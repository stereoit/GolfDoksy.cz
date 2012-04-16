from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView
from tournaments.models import Tournament
from tournaments.views import register_player

tournaments = Tournament.objects.all()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            model=Tournament, 
            context_object_name="tournament_list",
        ),
        name="tournaments",
    ),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(
            model=Tournament,
            context_object_name="tournament",
        ), 
        name="tournament_detail",
    ),
    url(r'^(?P<slug>[\w-]+)/prihlaseni/$', register_player, name="tournament_register"),
    url(r'^(?P<slug>[\w-]+)/odhlaseni/$', register_player, name="tournament_unregister"),
)
