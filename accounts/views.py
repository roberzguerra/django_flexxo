# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import RegistrationForm

class Register(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'