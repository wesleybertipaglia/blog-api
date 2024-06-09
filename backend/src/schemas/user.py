"""User schemas module."""
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """User schema - Signup"""
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
    username: Optional[str]
    name: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class UserSingle(BaseModel):
    """User schema - Single"""
    id: Optional[str] = None
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None
    picture: Optional[str] = None
    location: Optional[str] = None
    link: Optional[str] = None
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class UserUpdate(BaseModel):
    """User schema - Update"""
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None
    picture: Optional[str] = None
    location: Optional[str] = None
    link: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True
