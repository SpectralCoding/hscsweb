from django.conf.urls import patterns, url
from cardviewer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<request_cardid>.+)/$', views.carddata, name='carddata'),
    url(r'^cardlist$', views.cardlist, name='cardlist'),
    url(r'^metriclist$', views.metriclist, name='metriclist'),
]