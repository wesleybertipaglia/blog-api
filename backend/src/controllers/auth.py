"""Auth controller module."""

from src.schemas.auth import AuthSignIN, AuthSignUP, AuthUpdatePassword, AuthDelete
from src.repositories.auth import AuthRepository
from fastapi.responses import JSONResponse

class AuthController:
    """Auth controller class."""
    def __init__(self, db):
        self.db = db
        self.auth_repository = AuthRepository(db)

    def sign_in(self, auth: AuthSignIN) -> JSONResponse:
        """Sign in. (auth: AuthSignIN) -> JSONResponse."""
        return self.auth_repository.sign_in(auth)

    def sign_up(self, auth: AuthSignUP) -> JSONResponse:
        """Sign up. (auth: AuthSignUP) -> JSONResponse."""
        return self.auth_repository.sign_up(auth)
    
    def update_password(self, auth: AuthUpdatePassword, token: str) -> JSONResponse:
        """Update password. (auth: AuthUpdatePassword, token: str) -> JSONResponse."""
        return self.auth_repository.update_password(auth=auth, token=token)

    def delete(self, auth: AuthDelete, token: str) -> JSONResponse:
        """Delete an account. (auth: AuthDelete, token: str) -> JSONResponse."""
        return self.auth_repository.delete(auth=auth, token=token)
