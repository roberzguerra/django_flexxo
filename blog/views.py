# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render


def list(request):
    #question = get_object_or_404(Question, pk=question_id)

    return render(request, 'blog/list.html', {'item': 'Testeee....'})