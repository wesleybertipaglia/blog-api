"""User model module."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class UserModel (Base):
    """User model class"""
    __tablename__ = 'users'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    bio: Mapped[str] = mapped_column(String(255), nullable=True)
    picture: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    link: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    posts: Mapped['PostModel'] = relationship('PostModel', back_populates='user')
    likes: Mapped['LikeModel'] = relationship('LikeModel', back_populates='user')
    followers: Mapped['FollowModel'] = relationship('FollowModel', foreign_keys='FollowModel.followed_id', back_populates='followed')
    followeds: Mapped['FollowModel'] = relationship('FollowModel', foreign_keys='FollowModel.follower_id', back_populates='follower')
    comments: Mapped['CommentModel'] = relationship('CommentModel', back_populates='user')
