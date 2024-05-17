# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Collaborator, Event, Evaluation

# Create your tests here.


@login_required(login_url="/login/")
def evaluation_detail(request, id):
    if request.method == 'POST':
            return submitForm(request, id)
    
    event = get_object_or_404(Event, id_event=id)
    total = event.sheet.falta_just + event.sheet.falta_injust + event.sheet.respo + event.sheet.dispo + event.sheet.expert + event.sheet.produ
    if event.status_event == "Fechado":
        return render(request, 'home/finished.html', {'event': event, 'total' : total})
    return render(request, 'home/file.html', {'event': event})





@login_required(login_url="/login/")
def submitForm(request, id):
    event = request.POST.get('id_event')
    sheet = event.sheet
    respo = request.POST.get('respo')
    dispo = request.POST.get('dispo')
    expert = request.POST.get('expert')
    produ = request.POST.get('produ')
    falta_comment = request.POST.get('falta_comment')
    respo_comment = request.POST.get('respo_comment')
    dispo_comment = request.POST.get('dispo_comment')
    expert_comment = request.POST.get('expert_comment')
    produ_comment = request.POST.get('produ_comment')
    geral_comment = request.POST.get('geral_comment')
    sheet.respo = respo
    sheet.dispo = dispo
    sheet.expert = expert
    sheet.produ = produ
    sheet.falta_comment = falta_comment
    sheet.respo_comment = respo_comment
    sheet.dispo_comment = dispo_comment
    sheet.expert_comment = expert_comment
    sheet.produ_comment = produ_comment
    sheet.geral_comment = geral_comment
    event.status_event = "Fechado"
    total = event.sheet.falta_just + event.sheet.falta_injust + event.sheet.respo + event.sheet.dispo + event.sheet.expert + event.sheet.produ
    return render(request, 'home/finished.html', {'event': event, 'total' : total})
