from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str



class UserCreate(UserBase):
    password: str
    username: str
    role: int


class UserLogin(UserBase):
    password: str


class UserDetail(UserBase):
    username: str
    role: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True