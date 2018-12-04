# -*- coding:utf-8 -*-
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('registrar/', views.Register.as_view(), name='registration'),
]