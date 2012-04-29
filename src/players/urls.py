from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^prihlaseni/$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html'}, name='player-login'),
    url(r'^odhlaseni/$', 'django.contrib.auth.views.logout', {'template_name': 'players/logout.html'}, name='player-logout'),
    url(r'^registrace/$', 'django.contrib.auth.views.logout', name='player-registration'),
    url(r'^ajax/login/$', 'players.views.ajax_login',name="ajax_login"),
    url(r'^login/$', direct_to_template,{'template':'login.html'}, name="login"),
#    (r'^password_change/$', 'django.contrib.auth.views.password_change'),
#    (r'^password_change/done/$', 'django.contrib.auth.views.password_change_done'),
#    (r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
#    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
#    (r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm'),
#    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
