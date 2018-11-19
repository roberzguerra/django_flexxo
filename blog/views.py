# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Category

def list(request):
    #question = get_object_or_404(Question, pk=question_id)

    categories = Category.objects.all()


    # De acordo com as configuracoes de templates no settings.py, 
    # primeiro o django verifica se existe dentro do diretorio templates do proprio app (app blog/templates)
    # SE NAO encontrar, procura no diretorio template na raiz do projeto blog/list.html
    
    # utilizando o template do diretorio blog dentro de templates na raiz do projeto
    #return render(request, 'blog/list.html', {'item': 'Testeee....'})

    # utilizando o template do proprio diretorio templates do app blog
    return render(request, 'list.html', {'categories': categories})

def new(request):

    if request.POST:
        post = request.POST
        category = Category.objects.create(name=post.get('name'), description=post.get('description'))
        return redirect('blog-category-list')
    
    return render(request, 'new.html', {})




# Utilizando metodos separados para exibir a pagina de cadastro e cadastrar efetivamente:
# def new(request):
#     return render(request, 'new.html', {})

# def save(request):
#     if request.POST:
#         post = request.POST
#         category = Category.objects.create(name=post.get('name'), description=post.get('description'))
#     return redirect('blog-category-list')
    
