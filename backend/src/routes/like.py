"""Like routes module."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.like import Like, LikeList, LikeSingle
from src.controllers.like import LikeController
from src.core import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()

@router.get('/current', status_code=status.HTTP_200_OK, response_model=list[LikeList])
async def list_my_likes(token: str = Depends(security.oauth2_scheme)):
    """List likes from the current user. (token: str) -> LikeSingle."""
    return LikeController(db).list_my_likes(token)

@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=list[LikeList])
async def list_by_user(user_id: str):
    """List likes from a user. (user_id: str) -> LikeSingle."""
    return LikeController(db).list_by_user(user_id)

@router.get('/{post_id}', status_code=status.HTTP_200_OK, response_model=list[LikeList])
async def list(post_id: str):
    """List likes from a post. (post_id: str) -> LikeSingle."""
    return LikeController(db).list(post_id)

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=LikeSingle)
async def get(id: str):
    """Get a like by id. (id: str) -> LikeSingle."""
    return LikeController(db).get(id)

@router.get('/count/{post_id}', status_code=status.HTTP_200_OK)
async def count(post_id: str):
    """Count all likes from a post. (post_id: str) -> int."""
    return LikeController(db).count(post_id)

@router.post('/{post_id}', status_code=status.HTTP_201_CREATED, response_model=LikeSingle)
async def create(post_id: str, token: str = Depends(security.oauth2_scheme)):
    """Create a like in a post. (post_id: str, token: str) -> LikeSingle."""
    return LikeController(db).create(post_id=post_id, token=token)

@router.delete('/{post_id}', status_code=status.HTTP_200_OK)
async def delete(post_id: str, token: str = Depends(security.oauth2_scheme)):
    """Delete a like from a post. (post_id: str, token: str) -> JSONResponse."""
    return LikeController(db).delete(post_id=post_id, token=token)
