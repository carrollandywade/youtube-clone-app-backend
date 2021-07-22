from django.shortcuts import render
from .models import Reply
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ReplyList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class ReplyDetail(APIView):

    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
