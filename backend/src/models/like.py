"""Like model module."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class LikeModel (Base):
    """Like model class"""
    __tablename__ = 'likes'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'), nullable=False)
    post_id: Mapped[str] = mapped_column(String, ForeignKey('posts.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user: Mapped['UserModel'] = relationship("UserModel", back_populates="likes")
    post: Mapped['PostModel'] = relationship("PostModel", back_populates="likes")
