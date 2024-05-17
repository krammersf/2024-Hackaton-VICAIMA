
# python3 manage.py runserver
# python3 manage.py migrate
# python3 manage.py startapp myapp


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MasterUsers.settings')

import django
django.setup()

# Now you can import your Django models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    group = models.CharField(max_length=200, blank=True)
    permissions = models.JSONField()

class Admin(User):
    def save(self, *args, **kwargs):
        self.group = "ADMIN"
        self.permissions = {"ler": True, "editar": True}
        super().save(*args, **kwargs)

class Avaliador(User):
    def save(self, *args, **kwargs):
        self.group = "AVALIADOR"
        self.permissions = {"ler": True, "editar": "algumas"}
        super().save(*args, **kwargs)

class Avaliado(User):
    def save(self, *args, **kwargs):
        self.group = "REGULAR"
        self.permissions = {"ler": True, "editar": False}
        super().save(*args, **kwargs)
