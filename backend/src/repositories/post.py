"""Post repository module."""

import secrets
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.post import Post, PostSingle
from src.models.post import PostModel
from src.repositories.user import UserRepository

class PostRepository():
    """Post repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)
    
    def list(self, skip: int, limit: int) -> List[PostModel]:
        """List all posts with pagination. (skip: int, limit: int) -> List[PostModel]."""
        try:
            return self.db.query(PostModel).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_by_user(self, user_id: str, skip: int, limit: int) -> List[PostModel]:
        """List all posts from a user with pagination. (user_id: str, skip: int, limit: int) -> List[PostModel]."""
        try:
            return self.db.query(PostModel).filter(PostModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error
        
    def list_my_posts(self, token: str, skip: int, limit: int) -> List[PostModel]:
        """List all posts from the current user with pagination. (token: str, skip: int, limit: int) -> List[PostModel]."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            return self.db.query(PostModel).filter(PostModel.user_id == user_id).offset(skip).limit(limit).all()
        except Exception as error:
            raise error

    def get(self, id: str) -> PostModel:
        """Get a post by id. (id: str) -> PostModel."""
        try:
            post = self.db.query(PostModel).filter(PostModel.id == id).first()
            if not post:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found.")
            return post
        except Exception as error:
            raise error
    
    def create(self, post: Post, token: str) -> PostModel:
        """Create a new post. (post: PostModel, token: str) -> PostModel."""     
        try:
            user_id = self.user_repository.get_current_user_id(token)
            new_post = PostModel(**post.model_dump(exclude_unset=True, exclude={"user_id"}), slug=self.__create_slug(post.title), user_id=user_id)
            self.db.add(new_post)
            self.db.commit()
            self.db.refresh(new_post)
            return new_post
        except Exception as error:
            self.db.rollback()
            raise error

    def update(self, id: str, post: PostSingle, token: str) -> PostModel:
        """Update a post by id. (id: str, post: PostModel, token: str) -> PostModel."""
        try:
            self.__verify_owner(id, token)
            stored_post = self.get(id)
            for field in post.model_dump(exclude_unset=True):
                setattr(stored_post, field, getattr(post, field))
            self.db.commit()
            self.db.refresh(stored_post)
            return stored_post
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str, token: str) -> str:
        """Delete a post by id. (id: str, token: str) -> JSONResponse."""
        try:
            self.__verify_owner(id, token)
            post = self.get(id)
            self.db.delete(post)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Post deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
        
    def __get_by_slug(self, slug: str) -> PostModel:
        """Get a post by slug. (slug: str) -> PostModel."""
        return self.db.query(PostModel).filter(PostModel.slug == slug).first()

    def __create_slug(self, title: str) -> str:
        """Create a slug from post title. (title: str) -> str."""
        slug = title.lower().replace(" ", "-").replace(".", "").replace(",", "")
        if self.__get_by_slug(slug):
            slug = f"{slug}-{secrets.token_hex(2)}"
        return slug

    def __verify_owner(self, id: str, token: str) -> bool:
        """Verify if the user is the owner of the post. (id: str, token: str) -> bool."""
        try:
            user_id = self.user_repository.get_current_user_id(token)
            post = self.get(id)
            if post.user_id != user_id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not allowed.")
            return True
        except Exception as error:
            raise error