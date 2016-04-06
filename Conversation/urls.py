from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/show/$', views.show, name='show'),
	url(r'^(?P<pk>[0-9]+)/import/$', views.download, name='download'),
	url(r'^(?P<pk>[0-9]+)/sentiment/edit$', views.update_sentiment, name='update-sentiment'),
]