from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ISeaTeLContestSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ISeaTeLContestSite/admin/', include(admin.site.urls)),
    url(r'^ISeaTeLContestSite/rank/(?P<contest_id>[0-9]+)/$', 'contest.views.rank'),
    url(r'^$', 'index.views.home'),
    url(r'^contest/(?P<contest_id>[0-9]+)/$', 'contest.views.contest'),
)
