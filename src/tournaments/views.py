# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from models import Tournament

@login_required
def register_player(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)
    user = request.user
    tournament.players.add(user)
    messages.add_message(request, messages.INFO, 'Jste přihlášen/a k turnaji.')
    return HttpResponseRedirect(reverse('tournament_detail',kwargs={'slug': tournament.slug}))

@login_required
def unregister_player(request, slug):
    tournament = get_object_or_404(Tournament, slug=slug)
    user = request.user
    tournament.players.remove(user)
    messages.add_message(request, messages.INFO, 'Jste z turnaje odhlášen/a.')
    return HttpResponseRedirect(reverse('tournament_detail',kwargs={'slug': tournament.slug}))

