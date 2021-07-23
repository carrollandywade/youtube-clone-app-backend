from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer


class CommentList(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get_Comment(self, video_id):
        try:
            return Comment.objects.get(video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, video_id):
        comment = self.get_Comment(video_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, video_id):
        comment = self.get_Comment(video_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, video_id):
        comment = self.get_Comment(video_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Like(APIView):
    def get_Comment(self, video_id):
        try:
            return Comment.objects.get(video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def patch(self, request, video_id):
        comment = self.get_Comment(video_id)
        comment.like += 1
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dislike(APIView):
    def get_Comment(self, video_id):
        try:
            return Comment.objects.get(video_id=video_id)
        except Comment.DoesNotExist:
            raise Http404

    def patch(self, request, video_id):
        comment = self.get_Comment(video_id)
        comment.dislike += 1
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



