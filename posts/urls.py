
from django.urls import path
from . import views
from .views import TweetListView, TweetCreateView,TweetUpdateView,TweetDeleteView,TweetLikeView

app_name = "posts"

urlpatterns = [
  path('home/', TweetListView.as_view(), name='home'),
  path('tweet/<int:pk>/like', TweetLikeView.as_view(), name='tweetlike'),
  path('create_tweet/', TweetCreateView.as_view(), name='createtweet'),
  path('tweet/<int:pk>/update', TweetUpdateView.as_view(), name='tweetupdate'),
  path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweetdelete'),
]