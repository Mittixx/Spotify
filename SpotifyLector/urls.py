from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^$', views.home),
    url(r'^creator$', views.creator, name='creator'),
    url(r'^creator/auth$', views.creatorauth),

]

urlpatterns += staticfiles_urlpatterns()