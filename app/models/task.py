from tortoise import fields, models

class Task(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField()
    completed = fields.BooleanField(default=False)
    due_date = fields.DatetimeField(null=True, blank=True)
    owner = fields.ForeignKeyField("models.User", related_name="tasks")