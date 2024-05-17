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


@login_required(login_url="/login/")
def index(request):
    context = {
        'segment': 'index',
        'table' : Collaborator.objects.all()
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def infoDatabase(request):
    context = {
        'segment' : 'tables',
        'info' : Event.objects.all()
	}
    html_template = loader.get_template('home/tables.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
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

@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def dash_view(request):
    context = {
        'segment': 'dashboard',
        'table' : Event.objects.all()
    }

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


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
def submitForm(request, code):
    event = Event.objects.get(id_event=code)
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
    sheet.respo = int(respo)
    sheet.dispo = int(dispo)
    sheet.expert = int(expert)
    sheet.produ = int(produ)
    sheet.falta_comment = falta_comment
    sheet.respo_comment = respo_comment
    sheet.dispo_comment = dispo_comment
    sheet.expert_comment = expert_comment
    sheet.produ_comment = produ_comment
    sheet.geral_comment = geral_comment
    sheet.save()
    event.status_event = "Fechado"
    event.save()

    total = event.sheet.falta_just + event.sheet.falta_injust + event.sheet.respo + event.sheet.dispo + event.sheet.expert + event.sheet.produ
    return render(request, 'home/finished.html', {'event': event, 'total' : total})