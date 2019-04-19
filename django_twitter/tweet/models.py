from django.db import models
from django_twitter.twitteruser.models import TwitterUser


class Tweet(models.Model):

    body = models.CharField(max_length=140)
    time_stamp = models.DateTimeField(auto_now_add=True)
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-time_stamp',)

    def __str__(self):
        return self.body