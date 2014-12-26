from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ISeaTeLContestSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^ISeaTeLContestSite/admin/', include(admin.site.urls)),
    url(r'^ISeaTeLContestSite/rank/(?P<contest_id>[0-9]+)/$', 'contest.views.rank'),
    url(r'^ISeaTeLContestSite/competitor/(?P<contest_id>[0-9]+)/$', 'contest.views.competitor'),
    url(r'^$', 'index.views.home'),
    url(r'^judge/$', 'judge.views.home'),
    url(r'^problem/(?P<problem_id>[0-9]+)/$', 'problem.views.problem'),
    url(r'^contest/(?P<contest_id>[0-9]+)/$', 'contest.views.contest'),
)
