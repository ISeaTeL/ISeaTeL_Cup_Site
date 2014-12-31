from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^(?P<problem_id>[0-9]+)/$', views.problem, name='problem'),
	url(r'^status/$', views.status, name='status')
 )