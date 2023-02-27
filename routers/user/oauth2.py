import logging
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes, OAuth2PasswordRequestForm
from jose import jwt
from pydantic import ValidationError, UUID4
from sqlalchemy.orm import Session

from config import security
from config.config import settings
from config.security import verify_password
from db.session import get_db
from models.user.user import User
from schemas.user.token import TokenPayload
from utils.const import Role

oauth2 = APIRouter()

oauth2_bearer = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={
        Role.GUEST["name"]: Role.GUEST["description"],
        Role.ACCOUNT_ADMIN["name"]: Role.ACCOUNT_ADMIN["description"],
        Role.ACCOUNT_MANAGER["name"]: Role.ACCOUNT_MANAGER["description"],
        Role.ADMIN["name"]: Role.ADMIN["description"],
        Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
    },
)


@oauth2.post('/login')
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).get(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    if not user.user_role:
        role = Role.GUEST["name"]
    else:
        role = user.user_role.role.name

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_IN)

    token_payload = {
        "id": str(user.id),
        "role": role,
        "scopes": form_data.scopes
        # For security, you should make sure you only add the scopes that the user is actually able to have,
        # or the ones you have predefined.
    }
    return {
        "access_token": security.create_access_token(token_payload, expires_delta=access_token_expires),
        "token_type": "bearer",
    }


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def getuser(db: Session, id: UUID4):
    return db.query(User).filter(User.id == id).first()


async def get_current_user(security_scopes: SecurityScopes, db: Session = Depends(get_db), token: str = Depends(oauth2_bearer)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": authenticate_value}
                                          )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        if payload.get("id") is None:
            raise credentials_exception
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        logger.error("Error Decoding Token", exc_info=True)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")

    user = getuser(db, id=token_data.id)
    if not user:
        raise credentials_exception
    if security_scopes.scopes and not token_data.role:
        raise HTTPException(status_code=401, detail="Not enough permissions", headers={"WWW-Authenticate": authenticate_value})
    if security_scopes.scopes and token_data.role not in security_scopes.scopes:
        raise HTTPException(status_code=401, detail="Not enough permissions", headers={"WWW-Authenticate": authenticate_value})
    return user


@oauth2.get("/me")  # Get active current user
async def get_current_active_user(current_user: User = Security(get_current_user, scopes=[], )):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
