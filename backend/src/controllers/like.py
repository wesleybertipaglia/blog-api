"""Like controller module."""

from typing import List
from src.schemas.like import Like, LikeList, LikeSingle
from src.repositories.like import LikeRepository
from fastapi.responses import JSONResponse

class LikeController:
    """Like controller class."""
    def __init__(self, db):
        self.db = db
        self.like_repository = LikeRepository(db)

    def list(self, post_id: str, skip: int = 0, limit: int = 10) -> List[LikeList]:
        """List all likes of a post with pagination. (post_id: str, skip: int = 0, limit: int = 10) -> List[LikeList]."""
        return self.like_repository.list(post_id=post_id, skip=skip, limit=limit)
    
    def get(self, id: str) -> LikeSingle:
        """Get a like by id. (id: str) -> LikeSingle."""
        return self.like_repository.get(id)
    
    def count(self, post_id: str) -> JSONResponse:
        """Count all likes from a post. (post_id: str) -> int."""
        return self.like_repository.count(post_id)
    
    def create(self, like: Like) -> LikeSingle:
        """Create a like. (like: Like) -> LikeSingle."""
        return self.like_repository.create(like)
    
    def delete(self, post_id: str) -> JSONResponse:
        """Delete a like from a post. (post_id: str) -> JSONResponse."""
        return self.like_repository.delete(post_id)
