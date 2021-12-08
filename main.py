from typing import List, Tuple

import uvicorn
from fastapi import Depends, FastAPI, status
from tortoise.contrib.fastapi import register_tortoise

# modules import
from app.models import ArticleTortoise
from app.schemas import ArticleCreate, ArticleDB, ArticlePartialUpdate
from app.utils import get_article_or_404, pagination

api = FastAPI()


# create a new article
@api.post("/articles", response_model=ArticleDB, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleCreate) -> List[ArticleDB]:
    article_db = await ArticleTortoise.create(**article.dict())
    return ArticleDB.from_orm(article_db)


# get all articles
@api.get("/articles", response_model=List[ArticleDB])
async def get_articles(pagination: Tuple[int, int] = Depends(pagination)) -> List[ArticleDB]:
    skip, limit = pagination
    articles = await ArticleTortoise.all().offset(skip).limit(limit)
    results = [ArticleDB.from_orm(article) for article in articles]
    return results


# get a single article
@api.get("/articles/{article_id}", response_model=ArticleDB)
async def get_article(article_id: int) -> ArticleDB:
    article = await get_article_or_404(article_id)
    return ArticleDB.from_orm(article)


# update an article
@api.patch("/articles/{article_id}", response_model=ArticleDB)
async def update_article(
    article_update: ArticlePartialUpdate,
    article: ArticleTortoise = Depends(get_article_or_404),
) -> ArticleDB:
    article.update_from_dict(article_update.dict(exclude_unset=True))
    await article.save()
    return ArticleDB.from_orm(article)


# delete an article
@api.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article: ArticleTortoise = Depends(get_article_or_404)) -> None:
    await article.delete()


# add tortoise ORM Config
TORTOISE_ORM = {
    "connections": {"default": "sqlite://news.db"},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        },
    },
}

# register orm config
register_tortoise(
    api,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


# runserver
if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)
