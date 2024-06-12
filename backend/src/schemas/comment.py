"""Comment schema module."""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    """Comment schema - Base"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    post_id: str
    content: str
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class CommentList(BaseModel):
    """Comment schema - List"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    post_id: Optional[str] = None
    content: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class CommentSingle(BaseModel):
    """Comment schema - Single"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    post_id: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True