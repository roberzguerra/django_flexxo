"""django_flexxo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('blog/categorias', blog_views.list, name='blog-category-list'),
    path('blog/categorias/novo', blog_views.new, name='blog-category-new'),
    # Nao eh mais utilizado, a url acima supre esta abaixo.
    #path('blog/categorias/salvar', blog_views.save, name='blog-category-save'),

    path('blog/categorias/<int:id>', blog_views.edit, name='blog-category-edit'),
    path('blog/categorias/remover', blog_views.delete, name='blog-category-delete'),
    
]
