from django.db import models

# Create your models here.
class TodoList(models.Model):
    taskname = models.CharField(max_length = 100)
    done = models.BooleanField(default=False)