__author__ = 'rakot'

from django.conf.urls import patterns, url

from plays import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
