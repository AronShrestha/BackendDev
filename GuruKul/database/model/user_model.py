import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.dialects.postgresql import BYTEA as Bytea
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from sqlalchemy.types import LargeBinary
from database.database_config import Base
from database.model.mixin import Timestamp


class Role(enum.IntEnum):
    teacher = 1
    student = 2 


class User(Timestamp, Base):
    """
    Model for user
    
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
    username = Column(String(100))
    password = Column(LargeBinary)
    


