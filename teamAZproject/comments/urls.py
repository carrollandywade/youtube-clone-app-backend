from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:pk>/', views.CommentDetail.as_view(), name='comment'),
    path('replies/', views.ReplyList.as_view(), name='replies'),
    path('replies/<int:pk>/', views.ReplyDetail.as_view(), name='replies'),
    path('comments/likes/<int:pk>/', views.LikeDetail.as_view(), name='likes'),
    path('comments/dislikes/<int:pk>/', views.DislikeDetail.as_view(), name='dislikes')
]
