from django.urls import path
from django_twitter.tweet.views import add_tweet

urlpatterns = [
    path('add_tweet/', add_tweet, name='add_tweet')
]