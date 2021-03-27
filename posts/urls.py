from django.urls import path

from . import views
from .views import (LikeView, TweetDeleteView, TweetListView,
                    TweetUpdateView, create_post)

app_name = "posts"

urlpatterns = [
    path('home/', TweetListView.as_view(), name='home'),
    path('create_tweet/', create_post, name='createtweet'),
    path('tweet/<int:pk>/update', TweetUpdateView.as_view(), name='tweetupdate'),
    path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweetdelete'),
    path('like/<int:pk>', LikeView, name='like_tweet'),
]
