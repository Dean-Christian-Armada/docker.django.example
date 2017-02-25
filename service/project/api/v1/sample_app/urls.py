from django.conf.urls import url, include
from django.http import HttpResponse

from .import views

urlpatterns = [
 	url(r'^$', views.artists_list, name='artists-list'),
 	url(r'^(?P<artist_id>[0-9]+)/$', views.artist_detail, name='artists-detail'),
]