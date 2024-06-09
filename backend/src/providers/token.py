
import secrets
from fastapi import HTTPException, status
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta

class TokenProvider:
    """Token provider class"""
    def __init__(self):
        self.secret_key = secrets.token_urlsafe(32)
        self.algorithm = "HS256"
        self.access_token_expire_minutes = 60 * 24 * 1
        self.blacklist = []

    def create_access_token(self, data: dict):
        """Create an access token"""
        copy_data = data.copy()
        expire = datetime.now() + timedelta(minutes=self.access_token_expire_minutes)
        expire_timestamp = expire.timestamp()
        copy_data.update({"exp": expire_timestamp})
        return jwt.encode(copy_data, self.secret_key, algorithm=self.algorithm)
    
    def revoke_access_token(self, token: str):
        """Revoke an access token"""
        self.blacklist.append(token)
        expire = datetime.now()
        expire_timestamp = expire.timestamp()        
        return jwt.encode({"exp": expire_timestamp}, self.secret_key, algorithm=self.algorithm)
        
    def verify_token(self, token: str):
        """Verify a token"""
        if token in self.blacklist:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token revoked")

        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload.get("sub")
        except JWTError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")        
    