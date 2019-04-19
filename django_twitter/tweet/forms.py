from django import forms
from django_twitter.twitteruser.models import TwitterUser

class Add_Tweet(forms.Form):

    text = forms.CharField(widget=forms.Textarea)