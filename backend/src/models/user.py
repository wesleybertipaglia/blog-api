"""User model module."""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base

class UserModel (Base):
    """User model class"""
    __tablename__ = 'users'
    
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid4()))    
    username: Mapped[str] = mapped_column(String(14))    
    email: Mapped[str] = mapped_column(String(100))        
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str] = mapped_column(String(255))
    picture: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    link: Mapped[str] = mapped_column(String(255))    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
