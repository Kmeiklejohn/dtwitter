from django.db import models
from django_twitter.tweet.models import Tweet
from django_twitter.twitteruser.models import TwitterUser

class Notification(models.Model):

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    tagged = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
