# -*- coding: utf-8 -*-
from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext as _
import logging
from partners import models

log = logging.getLogger(__name__)
register = template.Library()

@register.inclusion_tag('fragments/partners.html', takes_context=True)
def partners_tag(context):
    context['partners'] = models.Partner.objects.filter(is_public=True).order_by('name')
    return context
