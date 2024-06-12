"""Post schema module."""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    """Post schema - Base"""
    id: Optional[str] = None
    title: str
    content: str
    picture: Optional[str] = None
    slug: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class PostList(BaseModel):
    """Post schema - List"""
    id: Optional[str] = None
    title: Optional[str] = None
    slug: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class PostSingle(BaseModel):
    """Post schema - Single"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    picture: Optional[str] = None
    slug: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True