"""Comment routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.comment import Comment, CommentList, CommentSingle
from src.controllers.comment import CommentController

router = APIRouter()
db: Session = next(get_db())

@router.get('/{post_id}', status_code=status.HTTP_200_OK, response_model=List[CommentList])
async def list(post_id: str, db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    """List all comments of a post with pagination. (post_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
    return CommentController(db).list(post_id=post_id, skip=skip, limit=limit)

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=CommentSingle)
async def get(id: str, db: Session = Depends(get_db)):
    """Get a comment by id. (id: str) -> CommentSingle."""
    return CommentController(db).get(id)

@router.get('/count/{post_id}', status_code=status.HTTP_200_OK)
async def count(post_id: str, db: Session = Depends(get_db)):
    """Count all comments. (post_id: str) -> JSONResponse."""
    return CommentController(db).count(post_id)

# Authentication is required to create, update and delete comments.
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommentSingle)
async def create(comment: Comment, db: Session = Depends(get_db)):
    """Create a comment. (comment: CommentSingle) -> CommentSingle."""
    return CommentController(db).create(comment)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=CommentSingle)
async def update(id: str, comment: CommentSingle, db: Session = Depends(get_db)):
    """Update a comment by id. (id: str, comment: CommentSingle) -> CommentSingle."""
    return CommentController(db).update(id=id, comment=comment)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete(id: str, db: Session = Depends(get_db)):
    """Delete a comment by id. (id: str) -> JSONResponse."""
    return CommentController(db).delete(id)