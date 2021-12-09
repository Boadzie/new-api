from typing import List

from fastapi import APIRouter, Depends, status
from tortoise.exceptions import DoesNotExist

from app.models.model import ArticleTortoise, CommentTortoise
from app.schemas.comment import CommentBase, CommentDB, CommentPartialUpdate
from app.utils import get_article_or_404, get_comment_or_404

router = APIRouter()


@router.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED, tags=["comments"])
async def create_comment(comment: CommentBase) -> CommentDB:
    try:
        await ArticleTortoise.get(id=comment.article_id)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Article {id} does not exist")
    comment_tortoise = await CommentTortoise.create(**comment.dict())
    return CommentDB.from_orm(comment_tortoise)


@router.get("/comments", response_model=List[CommentDB], tags=["comments"])
async def read_comments() -> List[CommentDB]:
    comments = await CommentTortoise.all()
    return [CommentDB.from_orm(comment) for comment in comments]


@router.get("/comments/{id}", response_model=CommentDB, tags=["comments"])
async def read_comment(id: int) -> CommentDB:
    try:
        comment = await CommentTortoise.get(id=id)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment {id} does not exist")
    return CommentDB.from_orm(comment)


# update a comment
@router.patch("/comment/{id}", response_model=CommentDB, tags=["comments"])
async def update_comment(
    comment_update: CommentPartialUpdate,
    comment: CommentTortoise = Depends(get_comment_or_404),
) -> CommentDB:
    comment.update_from_dict(comment_update.dict(exclude_unset=True))
    await comment.save()
    return CommentDB.from_orm(comment)


# delete a comment
@router.delete("/comments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["comments"])
async def delete_comment(comment: CommentTortoise = Depends(get_comment_or_404)) -> None:
    await comment.delete()
