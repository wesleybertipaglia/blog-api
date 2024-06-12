"""Follow routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.follow import Follow, FollowList, FollowSingle
from src.controllers.follow import FollowController
from src.core import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()


@router.get('/followers', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_followers(skip: int = 0, limit: int = 10, token: str = Depends(security.oauth2_scheme)):
    """List all followers of the current user with pagination. (skip: int = 0, limit: int = 10, token: str) -> List[FollowList]."""
    return FollowController(db).list_my_followers(skip=skip, limit=limit, token=token)

@router.get('/following', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_following(skip: int = 0, limit: int = 10, token: str = Depends(security.oauth2_scheme)):
    """List all following of the current user with pagination. (skip: int = 0, limit: int = 10, token: str) -> List[FollowList]."""
    return FollowController(db).list_my_following(skip=skip, limit=limit, token=token)

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=FollowSingle)
async def get(id: str):
    """Get a follow by id. (id: str) -> FollowSingle."""
    return FollowController(db).get(id)

@router.get('/followers/{user_id}', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_followers(user_id: str, skip: int = 0, limit: int = 10):
    """List all followers of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
    return FollowController(db).list_followers(user_id=user_id, skip=skip, limit=limit)

@router.get('/following/{user_id}', status_code=status.HTTP_200_OK, response_model=List[FollowList])
async def list_following(user_id: str, skip: int = 0, limit: int = 10):
    """List all following of a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[FollowList]."""
    return FollowController(db).list_following(user_id=user_id, skip=skip, limit=limit)

@router.get('/count/followers/{user_id}', status_code=status.HTTP_200_OK)
async def count_followers(user_id: str):
    """Count all followers. (user_id: str) -> JSONResponse."""
    return FollowController(db).count_followers(user_id)

@router.get('/count/following/{user_id}', status_code=status.HTTP_200_OK)
async def count_following(user_id: str):
    """Count all following. (user_id: str) -> JSONResponse."""
    return FollowController(db).count_following(user_id)

@router.post('/{user_id}', status_code=status.HTTP_201_CREATED, response_model=FollowSingle)
async def create(user_id: str, token: str = Depends(security.oauth2_scheme)):
    """Create a follow. (follow: FollowSingle, token: str) -> FollowSingle."""
    return FollowController(db).create(user_id=user_id, token=token)

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: str, token: str = Depends(security.oauth2_scheme)):
    """Delete a follow by id. (user_id: str, token: str) -> JSONResponse."""
    return FollowController(db).delete(user_id=user_id, token=token)