from typing import Tuple

from fastapi import Query

from app.models.model import ArticleTortoise, CommentTortoise


# pagination query
async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


# get a single Article with comment
async def get_article_or_404(id: int) -> ArticleTortoise:
    try:
        return await ArticleTortoise.get(id=id).prefetch_related("comments")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_comment_or_404(id: int) -> CommentTortoise:
    try:
        return await CommentTortoise.get(id=id).prefetch_related("article")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
