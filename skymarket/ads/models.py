from django.conf import settings
from django.db import models
from users.models import User

class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
