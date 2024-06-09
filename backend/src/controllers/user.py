"""User controller module."""
from typing import List
from fastapi import HTTPException, status
from src.schemas.user import UserList, UserSingle
from src.repositories.user import UserRepository

class UserController:
    """User controller class."""
    def __init__(self, db):
        self.db = db
        self.user_repository = UserRepository(db)

    def list(self, skip: int = 0, limit: int = 10) -> List[UserList]:
        """List all users with pagination. (skip: int = 0, limit: int = 10) -> List[UserList]."""
        return self.user_repository.list(skip, limit)
    
    def get(self, id: str) -> UserSingle:
        """Get a user by id. (id: str) -> UserSingle."""
        user = self.user_repository.get(id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found (404).")
        return user
