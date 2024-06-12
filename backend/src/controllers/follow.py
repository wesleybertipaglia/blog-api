"""Follow controller module."""

from typing import List
from src.schemas.follow import Follow, FollowList, FollowSingle
from src.repositories.follow import FollowRepository
from fastapi.responses import JSONResponse

class FollowController:
    """Follow controller class."""
    def __init__(self, db):
        self.db = db
        self.follow_repository = FollowRepository(db)

    def list_my_followers(self, token: str, skip: int = 0, limit: int = 10) -> List[FollowList]:
        """List all followers of the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
        return self.follow_repository.list_my_followers(skip=skip, limit=limit, token=token)
    
    def list_my_following(self, token: str, skip: int = 0, limit: int = 10) -> List[FollowList]:
        """List all following of the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
        return self.follow_repository.list_my_following(skip=skip, limit=limit, token=token)

    def list_followers(self, user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]:
        """List all followers of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
        return self.follow_repository.list_followers(user_id=user_id, skip=skip, limit=limit)
    
    def list_following(self, user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]:
        """List all following of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
        return self.follow_repository.list_following(user_id=user_id, skip=skip, limit=limit)
    
    def get(self, id: str) -> FollowSingle:
        """Get a follow by id. (id: str) -> FollowSingle."""
        return self.follow_repository.get(id)
    
    def count_followers(self, user_id: str) -> JSONResponse:
        """Count all followers. (user_id: str) -> JSONResponse."""
        return self.follow_repository.count_followers(user_id)
    
    def count_following(self, user_id: str) -> JSONResponse:
        """Count all following. (user_id: str) -> JSONResponse."""
        return self.follow_repository.count_following(user_id)
    
    def create(self, user_id: str, token: str) -> FollowSingle:
        """Create a follow. (user_id: str, token: str) -> FollowSingle."""
        return self.follow_repository.create(user_id=user_id, token=token)
    
    def delete(self, user_id: str, token: str) -> JSONResponse:
        """Stop following a user. (user_id: str, token: str) -> JSONResponse."""
        return self.follow_repository.delete(user_id=user_id, token=token)
