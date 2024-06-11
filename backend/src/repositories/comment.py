"""Comment repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.comment import Comment, CommentSingle
from src.models.comment import CommentModel
from src.core.security import Security

class CommentRepository():
    """Comment repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
    
    def list(self, post_id: str, skip: int, limit: int) -> List[CommentModel]:
        """List all comments of a post with pagination. (post_id: str, skip: int, limit: int) -> List[CommentModel]."""
        try:
            return self.db.query(CommentModel).filter(CommentModel.post_id == post_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error

    def get(self, id: str) -> CommentModel:
        """Get a comment by id. (id: str) -> CommentModel."""
        try:
            comment = self.db.query(CommentModel).filter(CommentModel.id == id).first()
            if not comment:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found.")
            return comment
        except Exception as error:
            raise error

    def count(self, post_id: str) -> JSONResponse:
        """Count all comments. (post_id: str) -> JSONResponse."""
        try:
            counts = self.db.query(CommentModel).filter(CommentModel.post_id == post_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": counts})
        except Exception as error:
            raise error

    def create(self, comment: Comment) -> CommentModel:
        """Create a new comment. (comment: CommentModel) -> CommentModel."""     
        try:            
            new_comment = CommentModel(**comment.model_dump(exclude_unset=True))
            self.db.add(new_comment)
            self.db.commit()
            self.db.refresh(new_comment)
            return new_comment
        except Exception as error:
            self.db.rollback()
            raise error

    def update(self, id: str, comment: CommentSingle) -> CommentModel:
        """Update a comment by id. (id: str, comment: CommentModel) -> CommentModel."""
        try:
            stored_comment = self.get(id)
            
            for field in comment.model_dump(exclude_unset=True):
                setattr(stored_comment, field, getattr(comment, field))

            self.db.commit()
            self.db.refresh(stored_comment)
            return stored_comment
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str) -> str:
        """Delete a comment by id. (id: str) -> JSONResponse."""
        try:
            comment = self.get(id)
            self.db.delete(comment)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Comment deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
