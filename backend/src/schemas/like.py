"""Like schema module."""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Like(BaseModel):
    """Like schema - Base"""
    id: Optional[str] = None
    user_id: str
    post_id: str
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class LikeList(BaseModel):
    """Like schema - List"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    post_id: Optional[str] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class LikeSingle(BaseModel):
    """Like schema - Single"""
    id: Optional[str] = None
    user_id: Optional[str] = None
    post_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration"""
        from_attributes = True