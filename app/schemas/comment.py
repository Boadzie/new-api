from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class CommentBase(BaseModel):
    article_id: int
    content: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class CommentPartialUpdate(BaseModel):
    content: Optional[str] = None


class CommentCreate(CommentBase):
    pass


class CommentDB(CommentBase):
    id: int
