from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


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
