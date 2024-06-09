from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashProvider:
    """Hash provider class"""
    def hash(self, password: str):
        """Hash a password"""
        return pwd_context.hash(password)

    def verify(self, hashed_password: str, plain_password: str):
        """Verify a password"""
        return pwd_context.verify(plain_password, hashed_password)
