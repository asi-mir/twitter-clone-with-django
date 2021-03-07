
from django.urls import path
from . import views
from .views import TweetListView, TweetCreateView,TweetUpdateView,TweetDeleteView

app_name = "post"

urlpatterns = [
  path('home/', TweetListView.as_view(), name='home'),
  path('create/', TweetCreateView.as_view(), name='createtweet'),
  path('tweet/<int:pk>/update', TweetUpdateView.as_view(), name='tweetupdate'),
  path('tweet/<int:pk>/delete', TweetDeleteView.as_view(), name='tweetdelete'),
]