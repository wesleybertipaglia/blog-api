"""Comment controller module."""

from typing import List
from src.schemas.comment import Comment, CommentList, CommentSingle
from src.repositories.comment import CommentRepository
from fastapi.responses import JSONResponse

class CommentController:
    """Comment controller class."""
    def __init__(self, db):
        self.db = db
        self.comment_repository = CommentRepository(db)

    def list(self, post_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]:
        """List all comments of a post with pagination. (post_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
        return self.comment_repository.list(post_id=post_id, skip=skip, limit=limit)
    
    def list_by_user(self, user_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]:
        """List all comments from a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
        return self.comment_repository.list_by_user(user_id=user_id, skip=skip, limit=limit)
    
    def list_my_comments(self, token: str, skip: int = 0, limit: int = 10) -> List[CommentList]:
        """List all comments from the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
        return self.comment_repository.list_my_comments(token=token, skip=skip, limit=limit)
    
    def get(self, id: str) -> CommentSingle:
        """Get a comment by id. (id: str) -> CommentSingle."""
        return self.comment_repository.get(id)
    
    def count(self, post_id: str) -> JSONResponse:
        """Count all comments. (post_id: str) -> JSONResponse."""
        return self.comment_repository.count(post_id)
    
    def create(self, comment: Comment, token: str) -> CommentSingle:
        """Create a comment. (comment: Comment, token: str) -> CommentSingle."""
        return self.comment_repository.create(comment=comment, token=token)
    
    def update(self, id: str, comment: CommentSingle, token: str) -> CommentSingle:
        """Update a comment by id. (id: str, comment: CommentSingle, token: str) -> CommentSingle."""
        return self.comment_repository.update(id=id, comment=comment, token=token)
    
    def delete(self, id: str, token: str) -> JSONResponse:
        """Delete a comment by id. (id: str, token: str) -> JSONResponse."""
        return self.comment_repository.delete(id=id, token=token)
