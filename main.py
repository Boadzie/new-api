from typing import List, Tuple

import uvicorn
from fastapi import Depends, FastAPI, status
from tortoise.contrib.fastapi import register_tortoise

# modules import
from app.models import ArticleTortoise
from app.schemas import ArticleBase, ArticleCreate, ArticleDB, ArticlePartialUpdate
from app.utils import get_article_or_404, pagination

api = FastAPI()


# create a new article
@api.post("/articles", response_model=ArticleDB, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleCreate):
    article_db = await ArticleTortoise.create(**article.dict())
    return ArticleDB.from_orm(article_db)


# get all articles
@api.get("/articles", response_model=List[ArticleBase], status_code=status.HTTP_200_OK)
async def get_articles(pagination: Tuple[int, int] = Depends(pagination)) -> List[ArticleDB]:
    skip, limit = pagination
    articles = await ArticleTortoise.all().offset(skip).limit(limit)

    results = [ArticleDB.from_orm(article) for article in articles]

    return results


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
