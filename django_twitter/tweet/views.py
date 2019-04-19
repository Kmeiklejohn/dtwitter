from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django_twitter.tweet.models import Tweet
from django_twitter.tweet.forms import Add_Tweet

@login_required()
def add_tweet(request):
    
    if request.method == "POST":
        form = Add_Tweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                body = data['text'],
                twitter_user = request.user.twitteruser
                )
            return render(request, 'success.html')
    else:
        form = Add_Tweet()
    return render(request, 'generic_form.html', {'form':form})
