# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Collaborator, Event, Evaluation

# Create your tests here.
@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def newEvent(request):
    if request.method == 'POST':
        return submitEvent(request)
    context = {
        'segment' : 'tables',
        'collaborators' : Collaborator.objects.all() 
	}
    html_template = loader.get_template('home/create_event.html')
    return HttpResponse(html_template.render(context, request))






@login_required(login_url="/login/")
def submitEvent(request):
    avaliador_id = request.POST.get('avaliador')
    avaliado_id = request.POST.get('avaliado')

    avaliador = Collaborator.objects.get(id=avaliador_id)
    avaliado = Collaborator.objects.get(id=avaliado_id)

    eval_sheet = Evaluation(evaluated=avaliado, evaluator=avaliador)
    eval_sheet.save()
    event = Event(evaluator_event=avaliador, evaluated_event=avaliado, sheet=eval_sheet)
    event.save()

    collaborators = Collaborator.objects.all()
    return render(request, 'home/create_event.html', {'collaborators': collaborators})
