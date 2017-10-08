from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    description = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
