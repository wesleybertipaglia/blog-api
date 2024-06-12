"""Like routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.like import Like, LikeList, LikeSingle
from src.controllers.like import LikeController

router = APIRouter()
db: Session = next(get_db())

@router.get('/{post_id}', status_code=status.HTTP_200_OK, response_model=list[LikeList])
async def list(post_id: str, db: Session = Depends(get_db)):
    """List likes from a post. (post_id: str) -> LikeSingle."""
    return LikeController(db).list(post_id)

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=LikeSingle)
async def get(id: str, db: Session = Depends(get_db)):
    """Get a like by id. (id: str) -> LikeSingle."""
    return LikeController(db).get(id)

@router.get('/count/{post_id}', status_code=status.HTTP_200_OK)
async def count(post_id: str, db: Session = Depends(get_db)):
    """Count all likes from a post. (post_id: str) -> int."""
    return LikeController(db).count(post_id)

# Authentication is required to create and delete likes.
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=LikeSingle)
async def create(like: Like, db: Session = Depends(get_db)):
    """Create a like. (like: LikeSingle) -> LikeSingle."""
    return LikeController(db).create(like)

@router.delete('/{post_id}', status_code=status.HTTP_200_OK)
async def delete(post_id: str, db: Session = Depends(get_db)):
    """Delete a like from a post. (post_id: str) -> JSONResponse."""
    return LikeController(db).delete(post_id)