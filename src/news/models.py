# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, force_unicode
import textile


class News(models.Model):
    title = models.CharField(_(u'title'), null=False, max_length=255)
    slug = models.CharField(_(u'slug'), max_length=255, editable=False, null=True)
    text = models.TextField(_(u'text'), null=False, blank=False,help_text=u'Text lze formárovat pomocí Textile.')
    text_html = models.TextField(_(u'text'), editable=False, null=True)
    published = models.DateTimeField(_(u'published'), null=False, blank=True)
    published_by = models.CharField(_(u'author'), max_length=255, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.text_html = force_unicode(textile.textile(smart_str(self.text),encoding='utf-8', output='utf-8'))
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'News')
        verbose_name_plural = _(u'News')
    
    def __unicode__(self):
        return self.title
