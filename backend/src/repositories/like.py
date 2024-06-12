"""Like repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.like import Like, LikeSingle
from src.models.like import LikeModel
from src.repositories.user import UserRepository

class LikeRepository():
    """Like repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
    
    def list(self, post_id: str, skip: int, limit: int) -> List[LikeModel]:
        """List all likes from a post with pagination. (post_id:int, skip: int, limit: int) -> List[LikeModel]."""
        try:
            return self.db.query(LikeModel).filter(LikeModel.post_id == post_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_by_user(self, user_id: str, skip: int, limit: int) -> List[LikeModel]:
        """List all likes from a user with pagination. (user_id: str, skip: int, limit: int) -> List[LikeModel]."""
        try:
            return self.db.query(LikeModel).filter(LikeModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_my_likes(self, token: str, skip: int, limit: int) -> List[LikeModel]:
        """List all likes from the current user with pagination. (token: str, skip: int, limit: int) -> List[LikeModel]."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            return self.db.query(LikeModel).filter(LikeModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error

    def get(self, id: str) -> LikeModel:
        """Get a like by id. (id: str) -> LikeModel."""
        try:
            return self.db.query(LikeModel).filter(LikeModel.id == id).first()
        except Exception as error:
            raise error
        
    def get_by_post_user(self, post_id: str, user_id: str) -> LikeModel:
        """Get a like by post id and user id. (post_id: str, user_id: str) -> LikeModel."""
        return self.db.query(LikeModel).filter(LikeModel.post_id == post_id, LikeModel.user_id == user_id).first()
        
    def count(self, post_id: str) -> JSONResponse:
        """Count all likes. (post_id: int) -> JSONResponse."""
        try:
            count = self.db.query(LikeModel).filter(LikeModel.post_id == post_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": count})
        except Exception as error:
            raise error

    def create(self, post_id: str, token: str) -> LikeModel:
        """Create a new like. (post_id: str, token: str) -> LikeModel."""     
        try:
            user_id = self.user_repository.get_current_user_id(token)
            if self.get_by_post_user(post_id=post_id, user_id=user_id):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Like already exists.")
            new_like = LikeModel(user_id=user_id, post_id=post_id)
            self.db.add(new_like)
            self.db.commit()
            self.db.refresh(new_like)
            return new_like
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, post_id: str, token: str) -> str:
        """Delete a like from a post. (post_id: str, token: str) -> JSONResponse."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            like = self.get_by_post_user(post_id=post_id, user_id=user_id)
            if not like:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Like not found.")
            self.db.delete(like)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Like deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
