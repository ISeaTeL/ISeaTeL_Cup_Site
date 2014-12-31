from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^(?P<contest_id>[0-9]+)/$', views.contest, name='contest'),
    url(r'^(?P<contest_id>[0-9]+)/feedback$', views.feedback, name='feedback'),
	url(r'^(?P<contest_id>[0-9]+)/signup$', views.signup, name='signup'),
    url(r'^(?P<contest_id>[0-9]+)/clarification$', views.clarification, name='clarification'),
    url(r'^(?P<contest_id>[0-9]+)/ISeaTeLContestSite/rank/$', views.rank),
    url(r'^(?P<contest_id>[0-9]+)/ISeaTeLContestSite/competitor/$', views.competitor),
    
)