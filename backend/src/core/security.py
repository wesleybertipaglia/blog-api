"""Security module."""

from providers.token import TokenProvider
from providers.hash import HashProvider

class Security:
    """Security class."""
    def __init__(self):
        self.token = TokenProvider()
        self.hash = HashProvider()

    def generate_token(self, data):
        """Generate a token from data. (data) -> token string"""
        return self.token.generate(data)

    def verify_token(self, token):
        """Verify a token. (token) -> bool"""
        return self.token.verify(token)

    def generate_hash(self, data):
        """Generate a hash from data. (data) -> hash string"""
        return self.hash.generate(data)

    def verify_hash(self, data, hash):
        """Verify a hash. (data, hash) -> bool"""
        return self.hash.verify(data, hash)
