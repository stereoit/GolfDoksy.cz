from tournaments.models import Tournament
import logging

log = logging.getLogger(__name__)

def have_tournaments(request):
    return {'have_tournaments': Tournament.objects.count() }
