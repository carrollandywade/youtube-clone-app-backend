from django.db import models


# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=1000, null=True)
    videoId = models.CharField(max_length=1000, null=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


class Reply(models.Model):
    replyToId = models.CharField(max_length=1000, null=True)
