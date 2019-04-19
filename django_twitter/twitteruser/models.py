from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitterhandle = models.CharField(max_length=50)
    follow = models.ManyToManyField('self', related_name='followed_by', blank=True)

    def __str__(self):
        return self.twitterhandle

