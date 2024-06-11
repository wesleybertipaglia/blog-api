"""User routes module."""

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.user import User, UserList, UserSingle
from src.controllers.user import UserController

router = APIRouter()
db: Session = next(get_db())

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserList])
async def list(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    """List all users with pagination. (skip: int = 0, limit: int = 10) -> List[UserList]."""
    return UserController(db).list(skip=skip, limit=limit)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserSingle)
async def get(id: str, db: Session = Depends(get_db)):
    """Get a user by id. (id: str) -> UserSingle."""
    return UserController(db).get(id)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSingle)
async def create(user: User, db: Session = Depends(get_db)):
    """Create a user. (user: UserSingle) -> UserSingle."""
    return UserController(db).create(user)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=UserSingle)
async def update(id: str, user: UserSingle, db: Session = Depends(get_db)):
    """Update a user by id. (id: str, user: UserSingle) -> UserSingle."""
    return UserController(db).update(id, user)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str, db: Session = Depends(get_db)):
    """Delete a user by id. (id: str) -> JSONResponse."""
    return UserController(db).delete(id)