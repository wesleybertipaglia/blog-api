"""Follow repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.follow import Follow, FollowSingle
from src.models.follow import FollowModel
from src.core.security import Security

class FollowRepository():
    """Follow repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
    
    def list_followers(self, user_id: str, skip: int, limit: int) -> List[FollowModel]:
        """List all followers with pagination. (user_id: str, skip: int, limit: int) -> List[FollowModel]."""
        try:
            return self.db.query(FollowModel).filter(FollowModel.followed_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_following(self, user_id: str, skip: int, limit: int) -> List[FollowModel]:
        """List all following with pagination. (user_id: str, skip: int, limit: int) -> List[FollowModel]."""
        try:
            return self.db.query(FollowModel).filter(FollowModel.follower_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error

    def get(self, id: str) -> FollowModel:
        """Get a follow by id. (id: str) -> FollowModel."""
        try:
            follow = self.db.query(FollowModel).filter(FollowModel.id == id).first()
            if not follow:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Follow not found.")
            return follow
        except Exception as error:
            raise error

    def count_followers(self, user_id: str) -> JSONResponse:
        """Count all followers. (user_id: str) -> JSONResponse."""
        try:
            count = self.db.query(FollowModel).filter(FollowModel.followed_id == user_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": count})
        except Exception as error:
            raise error
        
    def count_following(self, user_id: str) -> JSONResponse:
        """Count all following. (user_id: str) -> JSONResponse."""
        try:
            count = self.db.query(FollowModel).filter(FollowModel.follower_id == user_id).count()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"count": count})
        except Exception as error:
            raise error

    def create(self, follow: Follow) -> FollowModel:
        """Create a new follow. (follow: FollowModel) -> FollowModel."""     
        try:            
            new_follow = FollowModel(**follow.model_dump(exclude_unset=True))
            self.db.add(new_follow)
            self.db.commit()
            self.db.refresh(new_follow)
            return new_follow
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str) -> str:
        """Delete a follow by id. (id: str) -> JSONResponse."""
        try:
            follow = self.get(id)
            self.db.delete(follow)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Follow deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
