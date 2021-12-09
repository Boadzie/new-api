from typing import List, Tuple

from fastapi import APIRouter, Depends, status

from app.models.model import ArticleTortoise
from app.schemas.article import (
    ArticleBase,
    ArticleCreate,
    ArticleDB,
    ArticlePartialUpdate,
)
from app.utils import get_article_or_404, pagination

router = APIRouter()

# create a new article
@router.post("/articles", response_model=ArticleDB, status_code=status.HTTP_201_CREATED, tags=["articles"])
async def create_article(article: ArticleCreate) -> List[ArticleDB]:
    article_db = await ArticleTortoise.create(**article.dict())
    return ArticleDB.from_orm(article_db)


# get all articles
@router.get("/articles", response_model=List[ArticleDB], tags=["articles"])
async def get_articles(pagination: Tuple[int, int] = Depends(pagination)) -> List[ArticleDB]:
    skip, limit = pagination
    articles = await ArticleTortoise.all().offset(skip).limit(limit)
    results = [ArticleDB.from_orm(article) for article in articles]
    return results


# get a single article
@router.get("/articles/{article_id}", response_model=ArticleDB, tags=["articles"])
async def get_article(article_id: int) -> ArticleDB:
    article = await get_article_or_404(article_id)
    return ArticleDB.from_orm(article)


# update an article
@router.patch("/articles/{article_id}", response_model=ArticleDB, tags=["articles"])
async def update_article(
    article_update: ArticlePartialUpdate,
    article: ArticleTortoise = Depends(get_article_or_404),
) -> ArticleDB:
    article.update_from_dict(article_update.dict(exclude_unset=True))
    await article.save()
    return ArticleDB.from_orm(article)


# delete an article
@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["articles"])
async def delete_article(article: ArticleTortoise = Depends(get_article_or_404)) -> None:
    await article.delete()
