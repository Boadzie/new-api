from fastapi import APIRouter, status
from tortoise.exceptions import DoesNotExist

from app.models.model import ArticleTortoise, CommentTortoise
from app.schemas.comment import CommentBase, CommentDB

router = APIRouter()


@router.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentBase) -> CommentDB:
    try:
        await ArticleTortoise.get(id=comment.article_id)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Article {id} does not exist")
    comment_tortoise = await CommentTortoise.create(**comment.dict())
    return CommentDB.from_orm(comment_tortoise)
