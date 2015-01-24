from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^create$', views.create, {'g':''}),
    url(r'^change/(?P<url_hash>[0-9a-f]{32})/$', views.change, {'g':''}),
    url(r'^special_create$', views.create, {'g':'special_'}),
    url(r'^special_change/(?P<url_hash>[0-9a-f]{32})/$', views.change, {'g':'special_'}),

 )