"""User schemas module."""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    """User schema - Base"""
    id: Optional[str] = None
    username: str
    email: str
    password: str

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class UserList(BaseModel):
    """User schema - List"""
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class UserSingle(BaseModel):
    """User schema - Single"""
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    bio: Optional[str] = None
    picture: Optional[str] = None
    location: Optional[str] = None
    link: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

