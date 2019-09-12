from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """redirect automaticaly with CBV (Create)"""
        return reverse("myapp:post_detail", kwargs={'pk': self.pk})
