from django.conf.urls import patterns, url
from cardviewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))
