from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from tortoise import fields
from tortoise.models import Model


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


class ArticleTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    title = fields.CharField(max_length=100)
    body = fields.TextField()
    publication_date = fields.DatetimeField(null=False)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "articles"
