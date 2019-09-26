from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, by {}'.format(self.title, self.creator)
