"""Comment routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.comment import Comment, CommentList, CommentSingle
from src.controllers.comment import CommentController
from src.core import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()

@router.get('/current', status_code=status.HTTP_200_OK, response_model=List[CommentList])
async def list_my_comments(token: str = Depends(security.oauth2_scheme), skip: int = 0, limit: int = 10):
    """List all comments from the current user with pagination. (token: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
    return CommentController(db).list_my_comments(token=token, skip=skip, limit=limit)

@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=List[CommentList])
async def list_by_user(user_id: str, skip: int = 0, limit: int = 10):
    """List all comments from a user with pagination. (user_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
    return CommentController(db).list_by_user(user_id=user_id, skip=skip, limit=limit)

@router.get('/{post_id}', status_code=status.HTTP_200_OK, response_model=List[CommentList])
async def list(post_id: str, skip: int = 0, limit: int = 10):
    """List all comments of a post with pagination. (post_id: str, skip: int = 0, limit: int = 10) -> List[CommentList]."""
    return CommentController(db).list(post_id=post_id, skip=skip, limit=limit)

@router.get('/data/{id}', status_code=status.HTTP_200_OK, response_model=CommentSingle)
async def get(id: str):
    """Get a comment by id. (id: str) -> CommentSingle."""
    return CommentController(db).get(id)

@router.get('/count/{post_id}', status_code=status.HTTP_200_OK)
async def count(post_id: str):
    """Count all comments. (post_id: str) -> JSONResponse."""
    return CommentController(db).count(post_id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CommentSingle)
async def create(comment: Comment, token: str = Depends(security.oauth2_scheme)):
    """Create a comment. (comment: CommentSingle, token: str) -> CommentSingle."""
    return CommentController(db).create(comment=comment, token=token)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=CommentSingle)
async def update(id: str, comment: CommentSingle, token: str = Depends(security.oauth2_scheme)):
    """Update a comment by id. (id: str, comment: CommentSingle, token: str) -> CommentSingle."""
    return CommentController(db).update(id=id, comment=comment, token=token)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete(id: str, token: str = Depends(security.oauth2_scheme)):
    """Delete a comment by id. (id: str, token: str) -> JSONResponse."""
    return CommentController(db).delete(id=id, token=token)