"""Security module."""

from src.providers.token import TokenProvider
from src.providers.hash import HashProvider

class Security:
    """Security class."""
    def __init__(self):
        self.token = TokenProvider()
        self.hash = HashProvider()

    def generate_token(self, data) -> str:
        """Generate a token from data. (data) -> token string"""
        return self.token.generate(data)

    def verify_token(self, token: str) -> bool:
        """Verify a token. (token) -> bool"""
        return self.token.verify(token)

    def generate_hash(self, password: str) -> str:
        """Generate a hash from data. (password) -> hash string"""
        return self.hash.generate(password)

    def verify_hash(self, password: str, hash: str) -> bool:
        """Verify a hash. (password, hash) -> bool"""
        return self.hash.verify(plain_password=password, hashed_password=hash)
