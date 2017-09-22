from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^$', views.home),
    url(r'^creator$', views.creator, name='creator'),
    url(r'^creator/auth$', views.creatorauth),
    url(r'^postForm', views.postForm, name='postForm'),
    url(r'^playlistView', views.playlistView, name='playlistview'),
    url(r'^createPlaylist', views.createPlaylist, name='createPlaylist'),
    url(r'^end', views.end, name='end'),

]

urlpatterns += staticfiles_urlpatterns()