from typing import List, Tuple

import uvicorn
from fastapi import Depends, FastAPI, status
from tortoise.contrib.fastapi import register_tortoise

# modules import
from app.routers.articles import router as articles_router
from app.routers.comments import router as comments_router
from app.utils import get_article_or_404, pagination

# openapi_tags
tags_metadata = [
    {
        "name": "Articles",
        "description": "<h4>CRUD operation for Articles.<h4>",
    }
]

api = FastAPI(
    openapi_tags=tags_metadata,
    title="Newsman",
    description="<h3>News API with Articles, Comments and Best Practices<h3>",
    contact={
        "name": "Daniel Boadzie",
        "url": "https://boadzie.netlify.app",
        "email": "boadzie@gmail.com",
    },
)

# register routers
api.include_router(articles_router, prefix="/articles", tags=["articles"])
api.include_router(comments_router, prefix="/comments", tags=["comments"])

# add tortoise ORM Config
MODELS = ["app.models.model"]
TORTOISE_ORM = {
    "connections": {"default": "sqlite://news.db"},
    "apps": {"models": {"models": MODELS, "default_connection": "default"}},
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
