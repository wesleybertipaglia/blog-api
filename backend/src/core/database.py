from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:admin@localhost:5432/blog")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_db(seed: bool = False):
    """Create the database. (seed: bool = False) -> None"""
    try:
        Base.metadata.create_all(bind=engine)
        if seed:
            seed_db()
        print("Database created successfully")
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")

def seed_db():
    """Seed the database"""
    pass

def get_db():
    """Get the database. () -> SessionLocal"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
