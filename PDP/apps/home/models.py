# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Collaborator(models.Model):
    Nome = models.CharField(max_length=100, default="N/A")
    Apelido = models.CharField(max_length=100, default="N/A")
    Departamento = models.CharField(max_length=100, default="N/A")
    NumColab = models.IntegerField(default=0)
    NumAvali = models.IntegerField(default=0)
    Func = models.CharField(max_length=100, default="N/A")
    Data = models.CharField(max_length=10)
    Grupo = models.CharField(max_length=100, default="N/A")
    DirUni = models.IntegerField(default=0)
    
    def __str__(self):
        return "[" + str(self.NumColab) + "] " + self.Nome + " " + self.Apelido
    
class Evaluation(models.Model):
    evaluated = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name='+')
    falta_just = models.IntegerField(default=3)
    falta_injust = models.IntegerField(default=3)
    respo = models.IntegerField(default=3)
    dispo = models.IntegerField(default=3)
    expert = models.IntegerField(default=4)
    produ = models.IntegerField(default=4)
    falta_comment = models.CharField(max_length=100, default="")
    respo_comment = models.CharField(max_length=100, default="")
    dispo_comment = models.CharField(max_length=100, default="")
    expert_comment = models.CharField(max_length=100, default="")
    produ_comment = models.CharField(max_length=100, default="")
    geral_comment = models.CharField(max_length=300, default="")

    def __str__(self):
        return "E-" + str(self.evaluated.NumColab) + "-24"

def get_end_event():
    return timezone.now() + timedelta(days=10)

class Event(models.Model):
    id_event = models.BigAutoField(primary_key=True)
    evaluator_event = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    evaluated_event = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name='+')
    status_event = models.CharField(max_length=100, default="Aberto")
    start_event = models.DateTimeField(default=timezone.now)
    end_event = models.DateTimeField(default=get_end_event)
    sheet = models.ForeignKey(Evaluation, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "[" + str(self.id_event) + "]"