from django.db import models
from datetime import datetime

# создаем модель блогов
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title