"""Token provider module."""

import secrets
from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from datetime import datetime, timedelta

class TokenProvider:
    """Token provider class"""
    def __init__(self):
        self.secret_key = "OiJIUzI1NiIsInR5cCI6IkeyJzdWIiOiJOaWtvX1RvcnBAe"
        self.algorithm = "HS256"
        self.access_token_expire_minutes = 60 * 24 * 1  # 1 day

    def generate(self, data: dict) -> str:
        """Generate a token. (data: dict) -> str."""
        try:
            to_encode = data.copy()
            expire = datetime.now() + timedelta(minutes=self.access_token_expire_minutes)
            to_encode.update({"exp": expire})
            return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        except Exception as error:
            raise error
        
    def verify(self, token: str) -> dict:
        """Verify a token. (token: str) -> dict."""
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired.")
        except JWTError as error:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token: "+str(error))
        except Exception as error:
            raise error
