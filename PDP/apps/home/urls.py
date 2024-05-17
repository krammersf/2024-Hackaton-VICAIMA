# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

	path('tables/', views.infoDatabase, name='infoDatabase'), 
	path('tables/create_events/', views.newEvent, name='newEvent'),
	path('tables/<int:id>/file', views.evaluation_detail, name='evaluation_detail'),
    path('dashboard/', views.dash_view, name='dash_view'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]