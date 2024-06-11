"""User repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.user import User, UserSingle
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

    def create(self, user: User) -> UserModel:
        """Create a new user. (user: UserModel) -> UserModel."""     
        try:
            if self.get_by_email(user.email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
        
            if self.get_by_username(user.username):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered.")
            
            new_user = UserModel(**user.model_dump(exclude_unset=True, exclude={"password"}), password=self.security.generate_hash(password=user.password))
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except Exception as error:
            self.db.rollback()
            raise error

    def update(self, id: str, user: UserSingle) -> UserModel:
        """Update a user by id. (id: str, user: UserModel) -> UserModel."""
        try:
            stored_user = self.get(id)

            if user.email and user.email != stored_user.email:
                if self.get_by_email(user.email):
                    raise HTTPException(status_code=400, detail="Email already registered")
            
            if user.username and user.username != stored_user.username:
                if self.get_by_username(user.username):
                    raise HTTPException(status_code=400, detail="Username already registered")

            for field in user.model_dump(exclude_unset=True):
                setattr(stored_user, field, getattr(user, field))

            self.db.commit()
            self.db.refresh(stored_user)
            return stored_user
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str) -> str:
        """Delete a user by id. (id: str) -> JSONResponse."""
        try:
            user = self.get(id)
            self.db.delete(user)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "User deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
