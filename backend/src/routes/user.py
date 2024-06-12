"""User routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.user import UserList, UserSingle
from src.controllers.user import UserController
from src.core.security import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()

@router.get('/current', status_code=status.HTTP_200_OK, response_model=UserSingle)
async def get_current_user(token: str = Depends(security.oauth2_scheme)):
    """Get current user. (token: str) -> UserSingle."""
    return UserController(db).get_current_user(token)

@router.put('/', status_code=status.HTTP_200_OK, response_model=UserSingle)
async def update(user: UserSingle, token: str = Depends(security.oauth2_scheme)):
    """Update the current user. (user: UserSingle, token: str) -> UserSingle."""
    return UserController(db).update(user=user, token=token)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserList])
async def list(skip: int = 0, limit: int = 10):
    """List all users with pagination. (skip: int = 0, limit: int = 10) -> List[UserList]."""
    return UserController(db).list(skip=skip, limit=limit)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserSingle)
async def get(id: str):
    """Get a user by id. (id: str) -> UserSingle."""
    return UserController(db).get(id)
