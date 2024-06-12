"""User repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.schemas.user import UserSingle
from src.models.user import UserModel
from src.core.security import Security

class UserRepository():
    """User repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
    
    def list(self, skip: int, limit: int) -> List[UserModel]:
        """List all users with pagination. (skip: int, limit: int) -> List[UserModel]."""
        try:
            return self.db.query(UserModel).offset(skip).limit(limit).all()
        except Exception as error:
            raise error

    def get(self, id: str) -> UserModel:
        """Get a user by id. (id: str) -> UserModel."""
        try:
            user = self.db.query(UserModel).filter(UserModel.id == id).first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
            return user
        except Exception as error:
            raise error
    
    def get_by_email(self, email: str) -> UserModel:
        """Get a user by email. (email: str) -> UserModel."""
        return self.db.query(UserModel).filter(UserModel.email == email).first()          
    
    def get_by_username(self, username: str) -> UserModel:
        """Get a user by username. (username: str) -> UserModel."""
        return self.db.query(UserModel).filter(UserModel.username == username).first()

    def get_current_user(self, token: str) -> UserModel:
        """Get the current user. (token: str) -> UserModel."""
        try:
            payload = self.security.verify_token(token)
            email = payload.get("sub")
            user = self.get_by_email(email)
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
            return user
        except Exception as error:
            raise error
        
    def get_current_user_id(self, token: str) -> str:
        """Get the current user id. (token: str) -> str."""
        try:
            user = self.get_current_user(token)
            return user.id
        except Exception as error:
            raise error

    def update(self, user: UserSingle, token: str) -> UserModel:
        """Update the current user. (id: str, user: UserModel) -> UserModel."""
        try:
            current_user = self.get_current_user(token)
            if user.email and user.email != current_user.email:
                if self.get_by_email(user.email):
                    raise HTTPException(status_code=400, detail="Email already registered")            
            if user.username and user.username != current_user.username:
                if self.get_by_username(user.username):
                    raise HTTPException(status_code=400, detail="Username already registered")
            for field in user.model_dump(exclude_unset=True):
                setattr(current_user, field, getattr(user, field))
            self.db.commit()
            self.db.refresh(current_user)
            return current_user
        except Exception as error:
            self.db.rollback()
            raise error
