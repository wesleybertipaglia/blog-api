"""Auth routes module."""

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.auth import AuthSignIN, AuthSignUP, AuthDelete, AuthUpdatePassword
from src.schemas.user import UserSingle
from src.controllers.auth import AuthController
from src.core.security import Security

router = APIRouter()
db: Session = next(get_db())
security = Security()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserSingle)
async def sign_up(auth: AuthSignUP):
    """Sign up. (auth: AuthSignUP) -> UserSingle."""
    return AuthController(db).sign_up(auth)

@router.post('/signin', status_code=status.HTTP_200_OK)
async def sign_in(auth: AuthSignIN):
    """Sign in. (auth: AuthSignIN) -> Token."""
    return AuthController(db).sign_in(auth)

@router.put('/password', status_code=status.HTTP_200_OK)
async def update_password(auth: AuthUpdatePassword, token = Depends(security.oauth2_scheme)):
    """Update password. (auth: AuthUpdatePassword) -> JSONResponse."""
    return AuthController(db).update_password(auth=auth, token=token)

@router.delete('/delete', status_code=status.HTTP_200_OK)
async def delete(auth: AuthDelete, token = Depends(security.oauth2_scheme)):
    """Delete an account. (auth: AuthDelete) -> JSONResponse."""
    return AuthController(db).delete(auth=auth, token=token)
