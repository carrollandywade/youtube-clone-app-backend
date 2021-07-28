from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('comments/', views.CommentList.as_view(), name='comments'),
    path('comments/<str:videoId>', views.CommentDetail.as_view()),
    path('comments/likes/<str:comment_id>', views.Like.as_view()),
    path('comments/dislikes/<str:comment_id>', views.Dislike.as_view())
]
