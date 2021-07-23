from rest_framework import serializers
from .models import Comment
from .models import Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video_id', 'comment_to_video', 'like_video', 'dislike_video']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply_to_comment']
