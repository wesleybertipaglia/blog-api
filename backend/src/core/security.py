"""Security module."""

from fastapi.security import OAuth2PasswordBearer
from src.providers.token import TokenProvider
from src.providers.hash import HashProvider

class Security:
    """Security class."""
    def __init__(self):
        self.token = TokenProvider()
        self.hash = HashProvider()
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def generate_token(self, data: dict) -> str:
        """Generate a token from data. (data: dict) -> token string"""
        return self.token.generate(data)

    def verify_token(self, token: str):
        """Verify a token. (token: str) -> dict"""
        return self.token.verify(token)

    def generate_hash(self, password: str) -> str:
        """Generate a hash from data. (password: str) -> hash string"""
        return self.hash.generate(password)

    def verify_hash(self, password: str, hash: str) -> bool:
        """Verify a hash. (password: str, hash: str) -> bool"""
        return self.hash.verify(plain_password=password, hashed_password=hash)
