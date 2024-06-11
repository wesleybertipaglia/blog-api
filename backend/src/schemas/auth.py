"""Auth schema module."""

from typing import Optional
from pydantic import BaseModel

class AuthSignUP(BaseModel):
    """Auth schema - SignUP"""
    id: Optional[str] = None
    username: str
    email: str
    password: str
    
    class Config:
        """Pydantic configuration"""
        from_attributes = True

class AuthSignIN(BaseModel):
    """Auth schema - SignIN"""
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: str

    class Config:
        """Pydantic configuration"""
        from_attributes = True

class AuthDelete(BaseModel):
    """Auth schema - Delete"""
    id: Optional[str] = None
    password: str
    class Config:
        """Pydantic configuration"""
        from_attributes = True