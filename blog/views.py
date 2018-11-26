# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from blog.models import Category
from blog.forms import CategoryForm

def list(request):
    """
    Metodo para listagem de todas as categorias.
    """
    categories = Category.objects.all()

    # De acordo com as configuracoes de templates no settings.py, 
    # primeiro o django verifica se existe dentro do diretorio templates do proprio app (app blog/templates)
    # SE NAO encontrar, procura no diretorio template na raiz do projeto blog/list.html
    
    # utilizando o template do diretorio blog dentro de templates na raiz do projeto
    #return render(request, 'blog/list.html', {'item': 'Testeee....'})

    # utilizando o template do proprio diretorio templates do app blog
    return render(request, 'list.html', {'categories': categories})


def new(request):
    """
    Metodo para abrir a pagina de cadastro.
    E cadastrar 
    """
    form_url = reverse('blog-category-new')
    form = None
    if request.POST:

        form = CategoryForm(request.POST)
        if form.is_valid():
            
            category = form.save()

            # Criando mensagem de sucesso, somando strings (forma menos usual)
            messages.success(request, ('Categoria %s criada com sucesso.' % (category.name, )) )

            # Metodos para criar Messages:
            # messages.success(request, 'Profile details updated.')
            # messages.add_message(request, messages.SUCCESS, 'Registro cadastrado.')

            return redirect('blog-category-list')

    else:
        # Para carregar valores pre definidos no Form
        form = CategoryForm(initial={'name': '', 'description': '', 'created_at':''})
    return render(request, 'form.html', {'form': form, 'form_url': form_url})

def edit(request, id):
    """
    Metodo utilizado para editar/alterar o
    """
    # Busca normal do registro:
    #category = Category.objects.get(pk=id);

    # Busca com exception 404, se nao encontrar exibe erro 404
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(None, instance=category)

    if request.POST:

        form = CategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            
            category = form.save()
            messages.success(request, 'Categoria alterada.')
            return redirect('blog-category-list')

    form_url = reverse('blog-category-edit', args=(category.id, ))
    
    return render(request, 'form.html', {'category': category, 'form': form, 'form_url': form_url})


def delete(request):

    category = get_object_or_404(Category, pk=request.POST.get('id'))
    if category:
        category.delete()
        messages.success(request, 'Categoria removida.')

    return redirect('blog-category-list')

# def new(request):
#     """
#     Metodo para abrir a pagina de cadastro.
#     E cadastrar 
#     """
#     if request.POST:
#         post = request.POST
#         category = Category.objects.create(name=post.get('name'), description=post.get('description'))
#         return redirect('blog-category-list')
#     return render(request, 'new.html', {})

# Utilizando metodos separados para exibir a pagina de cadastro e cadastrar efetivamente:
# def new(request):
#     return render(request, 'new.html', {})

# def save(request):
#     if request.POST:
#         post = request.POST
#         category = Category.objects.create(name=post.get('name'), description=post.get('description'))
#     return redirect('blog-category-list')
