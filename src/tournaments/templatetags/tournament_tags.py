from django import template
from tournaments.models import Tournament
import logging

register = template.Library()
log = logging.getLogger(__name__)


@register.inclusion_tag('tournaments/tournament_table.html')
def render_tournaments(count=5):
    #return {'tournament_list': Tournament.objects.all()[:count]}
    tournament_list = Tournament.objects.all()[:count]
    return {'tournament_list': tournament_list }


@register.inclusion_tag('tournaments/register.html', takes_context=True)
def handle_registration(context, tournament):
    '''
    Add or remove the player from a tournament.
    '''
    already_registered = True if context['user'] in tournament.players.all() else False
    return { 
        'user': context['user'],
        'tournament': tournament,
        'already_registered': already_registered,
    }
