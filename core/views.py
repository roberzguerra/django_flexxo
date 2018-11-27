#-*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect, reverse

def home(request):

    return render(request, 'core/core.html', {})