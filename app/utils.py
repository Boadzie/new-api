from typing import Tuple

from fastapi import Query

from app.models.model import ArticleTortoise


# pagination query
async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


# get a single Article
async def get_article_or_404(id: int) -> ArticleTortoise:
    return await ArticleTortoise.get(id=id)
