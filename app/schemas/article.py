from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from app.schemas.comment import CommentDB


class ArticleBase(BaseModel):
    title: str
    body: str
    publication_date: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class ArticlePartialUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class ArticleCreate(ArticleBase):
    pass


class ArticleDB(ArticleBase):
    id: int


class PostPublic(ArticleDB):
    comments: List[CommentDB]

    @validator("comments", pre=True)
    def fetch_comments(cls, v):
        return list(v)
