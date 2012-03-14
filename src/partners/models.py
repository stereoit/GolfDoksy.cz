# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, force_unicode
import textile

class Partner(models.Model):
    name = models.CharField(_(u'title'), null=False, max_length=255)
    logo = models.ImageField(_(u'logo'), upload_to='partners')
    description = models.TextField(_(u'text'), null=False, blank=False,help_text=u'Text lze formárovat pomocí Textile.')
    description_html = models.TextField(_(u'text'), editable=False, null=True)
    is_public = models.BooleanField(_(u'is public'))

    def save(self, *args, **kwargs):
        self.description_html = force_unicode(textile.textile(smart_str(self.description),encoding='utf-8', output='utf-8'))
        super(Partner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'Partner')
        verbose_name_plural = _(u'Partners')
    
    def __unicode__(self):
        return self.name
