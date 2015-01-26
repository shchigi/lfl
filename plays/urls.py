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

    url(r'^roster/(?P<player_id>\d+)/$',
        'plays.views.player_details'),

    url(r'^cabinet/$',
        'plays.views.cabinet'),

    url(r'^cabinet/update_model/$',
        'plays.views.cabinet_update_model'),

    url(r'^cabinet/matches/$',
        'plays.views.cabinet_all_matches'),

    url(r'^cabinet/matches/(?P<id>\d+)/$',
        'plays.views.match_details'),

    url(r'^cabinet/matches/(?P<id>\d+)/goal/$',
        'plays.views.match_details_add_item',
        {'item': 'goal'}),

    url(r'^cabinet/settings/$',
        'plays.views.player_settings'),

    url(r'^bootstrap/$', 'plays.views.bootstrap')

)
