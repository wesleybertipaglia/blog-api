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
    
    def list_by_user(self, user_id: str, skip: int = 0, limit: int = 10) -> List[PostList]:
        """List all posts from a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[PostList]."""
        return self.post_repository.list_by_user(user_id=user_id, skip=skip, limit=limit)
    
    def list_my_posts(self, token: str, skip: int = 0, limit: int = 10) -> List[PostList]:
        """List all posts from the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[PostList]."""
        return self.post_repository.list_my_posts(token=token, skip=skip, limit=limit)
    
    def get(self, id: str) -> PostSingle:
        """Get a post by id. (id: str) -> PostSingle."""
        return self.post_repository.get(id)
    
    def create(self, post: Post, token: str) -> PostSingle:
        """Create a post. (post: Post, token: str) -> PostSingle."""
        return self.post_repository.create(post=post, token=token)
    
    def update(self, id: str, post: PostSingle, token: str) -> PostSingle:
        """Update a post by id. (id: str, post: PostSingle, token: str) -> PostSingle."""
        return self.post_repository.update(id=id, post=post, token=token)
    
    def delete(self, id: str, token: str) -> JSONResponse:
        """Delete a post by id. (id: str, token: str) -> JSONResponse."""
        return self.post_repository.delete(id=id, token=token)
