from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, by {}'.format(self.title, self.creator)


class UserLottie(models.Model):
    """https://lottiefiles.com/ : used for user profile animation"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    lottie_json = models.TextField()


class MyUser(AbstractUser):
    """delete validation constaints"""
    username = models.CharField(max_length=40, unique=True)
