"""Hash provider module."""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashProvider:
    """Hash provider class"""
    def generate(self, password: str):
        """Generate a hash from a password. (password: str) -> hash string"""
        return pwd_context.hash(password)

    def verify(self, hashed_password: str, plain_password: str):
        """Verify a password against a hash. (hash: str, password: str) -> bool"""
        return pwd_context.verify(plain_password, hashed_password)
