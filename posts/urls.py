from django.urls import path

from . import views
from .views import (LikeView, TweetCreateView, TweetDeleteView, TweetListView,
                    TweetUpdateView)

app_name = "posts"

urlpatterns = [
  path('home/', TweetListView.as_view(), name='home'),
  path('create_tweet/', TweetCreateView.as_view(), name='createtweet'),
  path('tweet/<int:pk>/update', TweetUpdateView.as_view(), name='tweetupdate'),
  path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweetdelete'),
  path('like/<int:pk>', LikeView ,name='like_tweet'),
]
