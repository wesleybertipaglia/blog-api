"""Follow model module."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class FollowModel (Base):
    """Follow model class"""
    __tablename__ = 'follows'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    follower_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'), nullable=False)
    followed_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    follower: Mapped['UserModel'] = relationship("UserModel", foreign_keys=[follower_id], back_populates="followers")
    followed: Mapped['UserModel'] = relationship("UserModel", foreign_keys=[followed_id], back_populates="followeds")
