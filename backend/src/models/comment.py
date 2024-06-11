"""Comment model module."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class CommentModel (Base):
    """"Comment model class"""
    __tablename__ = 'comments'

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.id'), nullable=False)
    post_id: Mapped[str] = mapped_column(String, ForeignKey('posts.id'), nullable=False)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    user: Mapped['UserModel'] = relationship("UserModel", back_populates="comments")
    post: Mapped['PostModel'] = relationship("PostModel", back_populates="comments")
