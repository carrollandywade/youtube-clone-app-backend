from django.db import models


# Create your models here.
class Comment(models.Model):
    video_Id = models.CharField(max_length=100)
    comment_to_video = models.CharField(max_length=100)
    like_video = models.IntegerField(default=0)
    dislike_video = models.IntegerField(default=0)
