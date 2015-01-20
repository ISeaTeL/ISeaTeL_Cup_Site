from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^create$', views.create),
    url(r'^change/(?P<url_hash>[0-9a-f]{32})/$', views.change),

 )