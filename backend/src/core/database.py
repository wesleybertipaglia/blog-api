from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:admin@localhost:5432/blog")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_db():
    """Create the database"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
