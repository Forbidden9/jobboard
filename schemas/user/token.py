from typing import List

from pydantic import BaseModel, UUID4


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    id: UUID4
    role: str = None
    scopes: List[str] = []
