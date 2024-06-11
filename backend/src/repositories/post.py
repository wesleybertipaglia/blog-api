"""Post repository module."""

import secrets
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.schemas.post import Post, PostSingle
from src.models.post import PostModel
from src.core.security import Security

class PostRepository():
    """Post repository class."""
    def __init__(self, db: Session):
        self.db = db
        self.security = Security()
    
    def list(self, skip: int, limit: int) -> List[PostModel]:
        """List all posts with pagination. (skip: int, limit: int) -> List[PostModel]."""
        try:
            return self.db.query(PostModel).offset(skip).limit(limit).all()
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
    
    def __get_by_slug(self, slug: str) -> PostModel:
        """Get a post by slug. (slug: str) -> PostModel."""
        return self.db.query(PostModel).filter(PostModel.slug == slug).first()

    def __create_slug(self, title: str) -> str:
        """Create a slug from post title. (title: str) -> str."""
        slug = title.lower().replace(" ", "-").replace(".", "").replace(",", "")
        if self.__get_by_slug(slug):
            slug = f"{slug}-{secrets.token_hex(2)}"
        return slug

    def create(self, post: Post) -> PostModel:
        """Create a new post. (post: PostModel) -> PostModel."""     
        try:            
            new_post = PostModel(**post.model_dump(exclude_unset=True, exclude={"slug"}), slug=self.__create_slug(post.title))
            self.db.add(new_post)
            self.db.commit()
            self.db.refresh(new_post)
            return new_post
        except Exception as error:
            self.db.rollback()
            raise error

    def update(self, id: str, post: PostSingle) -> PostModel:
        """Update a post by id. (id: str, post: PostModel) -> PostModel."""
        try:
            stored_post = self.get(id)
            
            for field in post.model_dump(exclude_unset=True):
                setattr(stored_post, field, getattr(post, field))

            self.db.commit()
            self.db.refresh(stored_post)
            return stored_post
        except Exception as error:
            self.db.rollback()
            raise error

    def delete(self, id: str) -> str:
        """Delete a post by id. (id: str) -> JSONResponse."""
        try:
            post = self.get(id)
            self.db.delete(post)
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Post deleted."})
        except Exception as error:
            self.db.rollback()
            raise error
