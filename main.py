import uvicorn
from fastapi import FastAPI, status
from tortoise.contrib.fastapi import register_tortoise

from app.models import ArticleTortoise
from app.schemas import ArticleBase, ArticleCreate, ArticleDB, ArticlePartialUpdate

api = FastAPI()


# create a new article
@api.post("/articles", response_model=ArticleDB, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleCreate):
    article_db = await ArticleTortoise.create(**article.dict())
    return ArticleDB.from_orm(article_db)


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
