"""User controller module."""

from typing import List
from src.schemas.user import User, UserList, UserSingle
from src.repositories.user import UserRepository
from fastapi.responses import JSONResponse

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
        return self.user_repository.get(id)
    
    def create(self, user: User) -> UserSingle:
        """Create a user. (user: User) -> UserSingle."""
        return self.user_repository.create(user)
    
    def update(self, id: str, user: UserSingle) -> UserSingle:
        """Update a user by id. (id: str, user: UserSingle) -> UserSingle."""
        return self.user_repository.update(id, user)
    
    def delete(self, id: str) -> JSONResponse:
        """Delete a user by id. (id: str) -> JSONResponse."""
        return self.user_repository.delete(id)
