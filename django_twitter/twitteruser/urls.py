from django.urls import path
from django_twitter.twitteruser.views import homepage_view, signup, login_view, index, profile_view, logout_view

urlpatterns = [
    path('index/', index, name="index"),
    path('', homepage_view, name='homepage'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout')
]

#test