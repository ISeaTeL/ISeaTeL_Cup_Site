from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ISeaTeLContestSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ISeaTeLContestSite/admin/', include(admin.site.urls)),
    
    url(r'^$', 'index.views.home'),

    url(r'^problem/', include('problem.urls')),
    url(r'^contest/', include('contest.urls')),
    url(r'^judge/', include('oj_judge.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^sudo/', include('sudo.urls')),

)
