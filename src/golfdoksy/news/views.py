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
from photologue import models

log = logging.getLogger(__name__)

#########
# Views #
#########

def news(request):
    c = RequestContext(request)
    c['news'] = News.objects.filter(published__lte=datetime.now()).order_by('-published')
    return render_to_response('news.html', c)

def gallery(request, slug = False):
    c = RequestContext(request)
    if slug:
        try:
            c['gallery'] = models.Gallery.objects.get(is_public=True, title_slug=slug)
            return render_to_response('gallery.html', c)
        except ObjectDoesNotExist:
            pass
    
    return render_to_response('galleries.html', c)
