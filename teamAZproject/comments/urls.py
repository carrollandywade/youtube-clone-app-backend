from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('comments/', views.CommentList.as_view(), name='comments'),
    path('comments/<str:video_id>', views.CommentDetail.as_view()),
    path('like/like/<str:video_id>', views.Like.as_view()),
    path('dislike/dislike/<str:video_id>', views.Dislike.as_view())
]
