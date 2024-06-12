"""Comment repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.comment import Comment, CommentSingle
from src.models.comment import CommentModel
from src.repositories.user import UserRepository

class CommentRepository():
    """Comment repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
    
    def list(self, post_id: str, skip: int, limit: int) -> List[CommentModel]:
        """List all comments of a post with pagination. (post_id: str, skip: int, limit: int) -> List[CommentModel]."""
        try:
            return self.db.query(CommentModel).filter(CommentModel.post_id == post_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_by_user(self, user_id: str, skip: int, limit: int) -> List[CommentModel]:
        """List all comments from a user with pagination. (user_id: str, skip: int, limit: int) -> List[CommentModel]."""
        try:
            return self.db.query(CommentModel).filter(CommentModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_my_comments(self, token: str, skip: int, limit: int) -> List[CommentModel]:
        """List all comments from the current user with pagination. (token: str, skip: int, limit: int) -> List[CommentModel]."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            return self.db.query(CommentModel).filter(CommentModel.user_id == user_id).offset(skip).limit(limit).all()
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
        
    def get_by_post_user(self, post_id: str, user_id: str) -> CommentModel:
        """Get a comment by post id and user id. (post_id: str, user_id: str) -> CommentModel."""
        return self.db.query(CommentModel).filter(CommentModel.post_id == post_id, CommentModel.user_id == user_id).first()

    def count(self, post_id: str) -> JSONResponse:
        """Count all comments. (post_id: str) -> JSONResponse."""
        try:
            counts = self.db.query(CommentModel).filter(CommentModel.post_id == post_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": counts})
        except Exception as error:
            raise error

    def create(self, comment: Comment, token: str) -> CommentModel:
        """Create a new comment. (comment: CommentModel, token: str) -> CommentModel."""     
        try:
            user_id = self.user_repository.get_current_user_id(token)
            new_comment = CommentModel(**comment.model_dump(exclude_unset=True, exclude={"user_id"}), user_id=user_id)
            self.db.add(new_comment)
            self.db.commit()
            self.db.refresh(new_comment)
            return new_comment
        except Exception as error:
            self.db.rollback()
            raise error

    def update(self, id: str, comment: CommentSingle, token: str) -> CommentModel:
        """Update a comment by id. (id: str, comment: CommentModel, token: str) -> CommentModel."""
        try:
            user_id = self.user_repository.get_current_user_id(token)            
            stored_comment = self.get(id)
            if stored_comment.user_id != user_id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to update this comment.")
            for field in comment.model_dump(exclude_unset=True, exclude={"user_id"}):
                setattr(stored_comment, field, getattr(comment, field))
            self.db.commit()
            self.db.refresh(stored_comment)
            return stored_comment
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str, token: str) -> str:
        """Delete a comment by id. (id: str, token: str) -> JSONResponse."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            comment = self.get(id)
            if comment.user_id != user_id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to delete this comment.")
            self.db.delete(comment)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Comment deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
