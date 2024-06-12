"""Follow repository module."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.follow import Follow, FollowSingle
from src.models.follow import FollowModel
from src.repositories.user import UserRepository

class FollowRepository():
    """Follow repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def list_my_followers(self, skip: int, limit: int, token: str) -> List[FollowModel]:
        """List all followers of the current user with pagination. (skip: int, limit: int, token: str) -> List[FollowModel]."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            return self.db.query(FollowModel).filter(FollowModel.followed_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_my_following(self, skip: int, limit: int, token: str) -> List[FollowModel]:
        """List all following of the current user with pagination. (skip: int, limit: int, token: str) -> List[FollowModel]."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            return self.db.query(FollowModel).filter(FollowModel.follower_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
    
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

    def create(self, user_id: str, token: str) -> FollowModel:
        """Create a new follow. (user_id: str, token: str) -> FollowModel."""     
        try:
            current_user_id = self.user_repository.get_current_user_id(token)
            follow = self.__get_follow(current_user_id, user_id)
            if follow:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You are already following this user.")
            new_follow = FollowModel(follower_id=current_user_id, followed_id=user_id)            
            self.db.add(new_follow)
            self.db.commit()
            self.db.refresh(new_follow)
            return new_follow
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, user_id: str, token: str) -> str:
        """Stop following a user. (user_id: str, token: str) -> JSONResponse."""
        try:
            current_user_id = self.user_repository.get_current_user_id(token)                      
            follow = self.__get_follow(follower_id=current_user_id, followed_id=user_id)
            if not follow:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You are not following this user.")
            self.db.delete(follow)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Follow deleted."})
        except Exception as error:
            self.db.rollback()
            raise error

    def __get_follow(self, follower_id: str, followed_id: str) -> FollowModel:
        """Get a follow by follower_id and followed_id. (follower_id: str, followed_id: str) -> FollowModel."""
        return self.db.query(FollowModel).filter(FollowModel.follower_id == follower_id, FollowModel.followed_id == followed_id).first()
