from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

PLAYER=0
MEMBER=1
PREMIUM_MEMBER=2

class PlayerProfile(models.Model):
    '''
    This class provides all necessary fields for players, they can also be 
    members of the club.
    '''
    MEMBERSHIP_CHOICES = (
        (PLAYER, _('Player')),
        (MEMBER, _('Member')),
        (PREMIUM_MEMBER, _('Premium Member')),
    )
    user = models.OneToOneField(User)
    has_paid = models.BooleanField(default=False)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, blank=True, default=PLAYER)

    def __unicode__(self):
        return u'%s' % self.get_membership_display()

def create_player_profile(sender, instance, created, **kwargs):
    '''
    Create player profile automatically for new users.
    '''
    if created:
        pass
        #PlayerProfile.objects.create(user=instance)

post_save.connect(create_player_profile, sender=User)
