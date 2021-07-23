from django.db import models


# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=100)
    comment_to_video = models.CharField(max_length=100)
    like_video = models.IntegerField(default=0)
    dislike_video = models.IntegerField(default=0)


class Reply(models.Model):
    reply_to_comment = models.CharField(max_length=100)
    comment = models.ForeignKey('comments.Comment', null=True, blank=True, on_delete=models.PROTECT)

