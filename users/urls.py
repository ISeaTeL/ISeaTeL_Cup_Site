from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^create/$', views.create),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
 )