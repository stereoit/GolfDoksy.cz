# -*- coding: utf-8 -*-
import logging
import django
import settings
from models import *
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from django.utils.datastructures import DotExpandedDict, SortedDict
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta, date
from cms.plugins import snippet
from datetime import datetime

log = logging.getLogger(__name__)

#########
# Views #
#########

def news(request):
    c = RequestContext(request)
    c['navigation'] = snippet.models.Snippet.objects.get(name='Navigation').html
    c['motto'] = snippet.models.Snippet.objects.get(name='Motto').html
    c['logo'] = snippet.models.Snippet.objects.get(name='Logo').html
    c['title'] = c['h2'] = u'Novinky'
    c['items'] = News.objects.filter(published__lte=datetime.now()).order_by('-published')
    return render_to_response('news-cms.tpl', c)

def media(request):
    c = RequestContext(request)
    c['navigation'] = snippet.models.Snippet.objects.get(name='Navigation').html
    c['motto'] = snippet.models.Snippet.objects.get(name='Motto').html
    c['logo'] = snippet.models.Snippet.objects.get(name='Logo').html
    c['title'] = c['h2'] = u'Média'
    c['items'] = Medium.objects.filter(published__lte=datetime.now()).order_by('-published')
    return render_to_response('news-cms.tpl', c)
