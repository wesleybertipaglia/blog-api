from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from uuid import uuid4
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True, index=True, default=str(uuid4()))
    email = Column(String)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(String, primary_key=True, index=True, default=str(uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    title = Column(String)
    content = Column(String)
    likescount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user = relationship('User', back_populates='posts')