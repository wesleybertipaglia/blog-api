from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas

# create ✅
def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(
        email=user.email,
        username=user.username,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# read ✅
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# update ✅
def update_user(db: Session, id: str, user: schemas.UserUpdate):
    existing_user = get_user(db, id)

    for field in user.model_dump(exclude_unset=True):
        setattr(existing_user, field, getattr(user, field))

    db.commit()
    db.refresh(existing_user)    
    return existing_user

# delete ✅
def delete_user(db: Session, id: str):
    user = get_user(db, id)        
    db.delete(user)
    db.commit()
    return {"message": "User deleted."}