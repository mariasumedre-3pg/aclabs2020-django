import uuid
from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    completed = models.BooleanField(default=False)
    text = models.TextField()
    priority = models.CharField(
        choices=(
            ('HIGH', 'High'),
            ('MEDIUM', 'Medium'),
            ('LOW', 'Low')
        ),
        default='LOW',
        max_length=50
    )
    due_date = models.DateField(null=True)
