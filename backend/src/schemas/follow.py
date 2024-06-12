"""Follow schema module."""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Follow(BaseModel):
    """Follow schema - Base"""
    id: Optional[str] = None
    follower_id: Optional[str] = None
    followed_id: str
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class FollowList(BaseModel):
    """Follow schema - List"""
    id: Optional[str] = None
    follower_id: Optional[str] = None
    followed_id: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class FollowSingle(BaseModel):
    """Follow schema - Single"""
    id: Optional[str] = None
    follower_id: Optional[str] = None
    followed_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True