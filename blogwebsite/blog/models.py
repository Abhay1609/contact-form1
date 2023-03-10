from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user import form


class Post(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)

    user=models.ForeignKey(User,on_delete=models.CASCADE , default=User)


    def __str__(self):
        return self.title
