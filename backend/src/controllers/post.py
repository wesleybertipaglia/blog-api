"""Post controller module."""

from typing import List
from src.schemas.post import Post, PostList, PostSingle
from src.repositories.post import PostRepository
from fastapi.responses import JSONResponse

class PostController:
    """Post controller class."""
    def __init__(self, db):
        self.db = db
        self.post_repository = PostRepository(db)

    def list(self, skip: int = 0, limit: int = 10) -> List[PostList]:
        """List all posts with pagination. (skip: int = 0, limit: int = 10) -> List[PostList]."""
        return self.post_repository.list(skip=skip, limit=limit)
    
    def get(self, id: str) -> PostSingle:
        """Get a post by id. (id: str) -> PostSingle."""
        return self.post_repository.get(id)
    
    def create(self, post: Post) -> PostSingle:
        """Create a post. (post: Post) -> PostSingle."""
        return self.post_repository.create(post)
    
    def update(self, id: str, post: PostSingle) -> PostSingle:
        """Update a post by id. (id: str, post: PostSingle) -> PostSingle."""
        return self.post_repository.update(id=id, post=post)
    
    def delete(self, id: str) -> JSONResponse:
        """Delete a post by id. (id: str) -> JSONResponse."""
        return self.post_repository.delete(id)
