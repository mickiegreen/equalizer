"""reango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from views import LoginView, SignUpView,RandomQueryView, RelevantArtistView, HatedGenreSongView, \
    PopularSongsView, MostLikedSongsView, MostUnlikedSongView,EqualizerView,LongestArtistSongView,\
    DislikeSongsView,SearchHistoryView,ShowHistoryPageView

urlpatterns = [
    url(r'^resources/users/login', LoginView.as_view()),
    url(r'^resources/users', csrf_exempt(SignUpView.as_view())),
    url(r'^resources/videos/mostUnliked', MostUnlikedSongView.as_view()),
    url(r'^resources/videos/mostlikedsongs', MostLikedSongsView.as_view()),
    url(r'^resources/videos/mostpopularsongs', PopularSongsView.as_view()),
    url(r'^resources/videos/equalizer', EqualizerView.as_view()),
    url(r'^resources/videos/hatedGenre', HatedGenreSongView.as_view()),
    url(r'^resources/videos/relevantView', RelevantArtistView.as_view()),
    url(r'^resources/videos/longestartistsong', LongestArtistSongView.as_view()),
    url(r'^resources/videos/randomQuery', RandomQueryView.as_view()),
    url(r'^resources/videos/dislikesongs', DislikeSongsView.as_view()),

    url(r'^resources/videos/searchhistoryview', SearchHistoryView.as_view()),
    url(r'^resources/videos/showhistorypage', ShowHistoryPageView.as_view()),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
    ]