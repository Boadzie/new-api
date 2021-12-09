from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class CommentTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    content = fields.TextField(null=False)
    article = fields.ForeignKeyField("models.ArticleTortoise", related_name="comments", null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        table = "comments"


class ArticleTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    title = fields.CharField(max_length=100)
    body = fields.TextField()
    publication_date = fields.DatetimeField(null=False)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        table = "articles"
