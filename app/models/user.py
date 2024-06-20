from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    hashed_password = fields.CharField(max_length=128)
    tasks = fields.ReverseRelation["Task"]