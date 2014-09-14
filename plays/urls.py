__author__ = 'rakot'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),

    url(r'^index/$',
        'plays.views.index'),

    url(r'^roster/$',
        'plays.views.roster'),

    url(r'^roster/(?P<player_id>\d+)/',
        'plays.views.player_details')
)
