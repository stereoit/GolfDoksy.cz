from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime,timedelta
from django.contrib.auth.models import User


'''
Tournament in the golf club
'''
class Tournament(models.Model):
    name = models.CharField(_('name'), max_length=160, help_text=_('the name of the tournament'))
    slug = models.SlugField(_('slug name'),max_length=160, help_text=_('Name in the URL'), unique=True)
    starts_on = models.DateTimeField(_('start time'), blank=True, null=True, help_text=_('Datetime of start'))
    is_listed = models.BooleanField(_('is listed'), default=True, help_text=_('Is the tournament listed?'))
    description = models.TextField(_('description'), blank=True, help_text=_('long description'))
    players = models.ManyToManyField(User, help_text=_('Participating players'), null=True, blank=True)



    def is_closed(self):
        return datetime.now() > (self.starts_on +timedelta(day=1))

    class Meta:
        ordering = ['-starts_on']
        verbose_name = _('tournament')
        verbose_name_plural = _('tournaments')


    def __unicode__(self):
        return self.name

