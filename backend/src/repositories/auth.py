"""Auth repository module."""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.auth import AuthSignIN, AuthSignUP, AuthUpdatePassword, AuthDelete, AuthToken
from src.models.user import UserModel
from src.core.security import Security
from src.repositories.user import UserRepository

class AuthRepository():
    """Auth repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
        self.user_repository = UserRepository(db)

    def sign_up(self, auth: AuthSignUP) -> UserModel:
        """Sign UP. (auth: AuthSignUP) -> UserModel."""     
        try:
            if self.user_repository.get_by_email(auth.email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
        
            if self.user_repository.get_by_username(auth.username):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Authname already registered.")
            
            new_user = UserModel(**auth.model_dump(exclude_unset=True, exclude={"password"}), password=self.security.generate_hash(password=auth.password))
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except Exception as error:
            self.db.rollback()
            raise error

    def sign_in(self, auth: AuthSignIN) -> AuthToken:
        """Sign IN. (auth: AuthSignIN) -> UserModel."""
        try:
            user = None
            if auth.email:
                user = self.user_repository.get_by_email(auth.email)
            elif auth.username:
                user = self.user_repository.get_by_username(auth.username)
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
            if not self.security.verify_hash(password=auth.password, hash=user.password):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
            token = self.security.generate_token(data={"sub": user.email})
            return AuthToken(access_token=token)
        except Exception as error:
            raise error
          
    def update_password(self, auth: AuthUpdatePassword, token: str) -> JSONResponse:
        """Update password. (auth: AuthUpdatePassword, token: str) -> JSONResponse."""
        try:
            user = self.user_repository.get_current_user(token)
            if not self.security.verify_hash(password=auth.password, hash=user.password):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
            user.password = self.security.generate_hash(password=auth.new_password)
            self.db.commit()
            return JSONResponse(content={"message": "Password updated."})
        except Exception as error:
            self.db.rollback()
            raise error
        
    def delete(self, auth: AuthDelete, token: str) -> JSONResponse:
        """Delete an account. (auth: AuthDelete, token: str) -> JSONResponse."""
        try:
            user = self.user_repository.get_current_user(token)
            if not self.security.verify_hash(password=auth.password, hash=user.password):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
            self.db.delete(user)
            self.db.commit()
            return JSONResponse(content={"message": "Account deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
