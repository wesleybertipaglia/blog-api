"""User repository module."""
from typing import List
from sqlalchemy.orm import Session
from src.models.user import UserModel
from src.schemas.user import UserList, UserSingle

class UserRepository():
    """User repository class."""
    def __init__(self, db: Session):
        self.db = db
    
    def list(self, skip: int, limit: int) -> List[UserList]:
        """List all users with pagination. (skip: int, limit: int) -> List[UserList]."""
        return self.db.query(UserModel).offset(skip).limit(limit).all()

    def get(self, id: str) -> UserSingle:
        """Get a user by id. (id: str) -> UserSingle."""
        return self.db.query(UserModel).filter(UserModel.id == id).first()
