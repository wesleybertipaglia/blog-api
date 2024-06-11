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
    
    def create(self, follow: Follow) -> FollowSingle:
        """Create a follow. (follow: Follow) -> FollowSingle."""
        return self.follow_repository.create(follow)
    
    def delete(self, id: str) -> JSONResponse:
        """Delete a follow by id. (id: str) -> JSONResponse."""
        return self.follow_repository.delete(id)
