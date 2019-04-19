from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django_twitter.twitteruser.models import TwitterUser, User
from django_twitter.twitteruser.forms import Add_TwitterUser, SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django_twitter.tweet.models import Tweet
from django.contrib.auth.decorators import login_required


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username = data['username'],
                email = data['email'],
                password = data['password']
            )
            login(request, user)
            TwitterUser.objects.create(
                twitterhandle = data['twitterhandle'],
                user = user
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignupForm()
    return render(request, 'generic_form.html', {'form':form})

def login_view(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    else:
        form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='index')
def homepage_view(request):
    if request.user:
        current_user = TwitterUser.objects.filter(user=request.user)
        user_tweets = Tweet.objects.filter(twitter_user=current_user)
        tweets = Tweet.objects.all()

        data = {
        "tweets": tweets,
        "user_tweets": user_tweets,
        "current_user": current_user
        }
        return render(request, 'homepage.html', data)
    return HttpResponseRedirect(reverse('index'))

def index(request):
  return render(request, 'index.html')



def profile_view(request):

  user = User.objects.get(username=request.user)


  return render(request, 'profile.html', {'user': user})