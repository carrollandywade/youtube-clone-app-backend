from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CommentList(APIView):
    def get(self, request):
        comment = Comment.object.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self, pk):
        pass

    def put(self, request, pk):
        pass

# Create your views here.
class ReplyList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class ReplyDetail(APIView):

    def get_object(self, pk):
        pass

    def put(self, request, pk):
        pass
