from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import controllers, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/')
def home():
    return 'Welcome to blog api 🎉.'

# create ✅
@app.post("/api/v1/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return controllers.create_user(db, user)

# read ✅
@app.get("/api/v1/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return controllers.get_users(db, skip=skip, limit=limit)

@app.get("/api/v1/users/{id}", response_model=schemas.User)
async def read_user(id: str, db: Session = Depends(get_db)):
    return controllers.get_user(db, id)

# update ✅
@app.put("/api/v1/users/{id}", response_model=schemas.User)
async def update_user(id: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return controllers.update_user(db, id, user)

# delete ✅
@app.delete("/api/v1/users/{id}")
async def delete_user(id: str, db: Session = Depends(get_db)):
    return controllers.delete_user(db, id)    