# -*- coding:utf-8 -*-
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('registrar/', views.SignUp.as_view(), name='registration'),
]