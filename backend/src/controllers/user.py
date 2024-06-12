"""User controller module."""

from typing import List
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
        return self.user_repository.get(id)
    
    def get_current_user(self, token: str):
        """Get current user. (token: str) -> UserSingle."""
        return self.user_repository.get_current_user(token)
    
    def update(self, user: UserSingle, token: str) -> UserSingle:
        """Update a user by id. (user: UserSingle, token: str) -> UserSingle."""
        return self.user_repository.update(user=user, token=token)
