from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail, name='comment'),
    path('replies/', views.ReplyList.as_view()),
    path('replies/<int:pk>/', views.CommentDetail, name='comment')
]
