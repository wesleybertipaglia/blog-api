"""Like repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.like import Like, LikeSingle
from src.models.like import LikeModel
from src.core.security import Security

class LikeRepository():
    """Like repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
    
    def list(self, post_id: str, skip: int, limit: int) -> List[LikeModel]:
        """List all likes from a post with pagination. (post_id:int, skip: int, limit: int) -> List[LikeModel]."""
        try:
            return self.db.query(LikeModel).filter(LikeModel.post_id == post_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def get(self, id: str) -> LikeModel:
        """Get a like by id. (id: str) -> LikeModel."""
        try:
            return self.db.query(LikeModel).filter(LikeModel.id == id).first()
        except Exception as error:
            raise error
        
    def count(self, post_id: str) -> JSONResponse:
        """Count all likes. (post_id: int) -> JSONResponse."""
        try:
            count = self.db.query(LikeModel).filter(LikeModel.post_id == post_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": count})
        except Exception as error:
            raise error

    def create(self, like: Like) -> LikeModel:
        """Create a new like. (like: LikeModel) -> LikeModel."""     
        try:            
            new_like = LikeModel(**like.model_dump(exclude_unset=True))
            self.db.add(new_like)
            self.db.commit()
            self.db.refresh(new_like)
            return new_like
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, post_id: str) -> str:
        """Delete a like from a post. (post_id: str) -> JSONResponse."""
        try:
            like = self.get(post_id)
            self.db.delete(like)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Like deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
