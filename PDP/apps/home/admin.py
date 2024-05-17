# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Collaborator
from .models import Event
from .models import Evaluation
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Collaborator, ImportExportModelAdmin)
admin.site.register(Event, ImportExportModelAdmin)
admin.site.register(Evaluation, ImportExportModelAdmin)
# Need to create a new model for json, so we can upload the json file by the admin page
# Or if we dont want, we can still upload the excel folder from admin page.
# If the superuser (admin or RH?) wants to add a new Collaborator, they can do by clicking on ADD COLABORATORS too
# =)