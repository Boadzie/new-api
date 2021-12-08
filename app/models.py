from tortoise import fields
from tortoise.models import Model


class ArticleTortoise(Model):
    id = fields.IntField(pk=True, generated=True)
    title = fields.CharField(max_length=100)
    body = fields.TextField()
    publication_date = fields.DatetimeField(null=False)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "articles"
