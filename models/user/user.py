import uuid
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import String, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    fullname = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(13), unique=True, index=True, nullable=True)
    password = Column(String(255), nullable=False, unique=True)  # hashed_password
    photo = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    user_role = relationship("UserRole", back_populates="user", uselist=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # verified = Column(Boolean, nullable=False, server_default='False')
    # verification_code = Column(String, nullable=True, unique=True)
