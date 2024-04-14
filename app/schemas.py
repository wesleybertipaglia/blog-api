from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    first_name: str
    last_name: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: UUID    
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        orm_mode = True

class PostBase(BaseModel):    
    title: str
    content: str
    likes_count: int

class Post(PostBase):
    id: UUID
    user_id: UUID    
    created_at: datetime

    class Config:
        orm_mode = True