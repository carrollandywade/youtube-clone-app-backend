from django.db import models


# Create your models here.
class Reply(models.Model):
    reply_to_comment = models.CharField(max_length=100)

