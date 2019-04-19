from django import forms
from django_twitter.twitteruser.models import TwitterUser, User

class Add_TwitterUser(forms.Form):
    twitterhandle = forms.CharField(max_length=50)
    user = forms.ModelChoiceField(
        queryset=User.objects.all())

class SignupForm(forms.Form):
    
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    twitterhandle= forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())