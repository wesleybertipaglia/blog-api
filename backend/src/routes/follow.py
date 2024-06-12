"""Follow routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.follow import Follow, FollowList, FollowSingle
from src.controllers.follow import FollowController

router = APIRouter()
db: Session = next(get_db())

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=FollowSingle)
async def get(id: str, db: Session = Depends(get_db)):
    """Get a follow by id. (id: str) -> FollowSingle."""
    return FollowController(db).get(id)

@router.get('/followers/{user_id}', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_followers(user_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List all followers of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
    return FollowController(db).list_followers(user_id=user_id, skip=skip, limit=limit)

@router.get('/following/{user_id}', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_following(user_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List all following of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
    return FollowController(db).list_following(user_id=user_id, skip=skip, limit=limit)

@router.get('/count/followers/{user_id}', status_code=status.HTTP_200_OK)
async def count_followers(user_id: str, db: Session = Depends(get_db)):
    """Count all followers. (user_id: str) -> JSONResponse."""
    return FollowController(db).count_followers(user_id)

@router.get('/count/following/{user_id}', status_code=status.HTTP_200_OK)
async def count_following(user_id: str, db: Session = Depends(get_db)):
    """Count all following. (user_id: str) -> JSONResponse."""
    return FollowController(db).count_following(user_id)

# Authentication is required to create and delete follows.
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=FollowSingle)
async def create(follow: Follow, db: Session = Depends(get_db)):
    """Create a follow. (follow: FollowSingle) -> FollowSingle."""
    return FollowController(db).create(follow)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str, db: Session = Depends(get_db)):
    """Delete a follow by id. (id: str) -> JSONResponse."""
    return FollowController(db).delete(id)