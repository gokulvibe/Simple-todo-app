from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    owner = models.ForeignKey(User,verbose_name = 'User', related_name = 'TodoLists',on_delete=models.CASCADE)
    taskname = models.CharField(max_length = 100)
    done = models.BooleanField(default=False)