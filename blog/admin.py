# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    """
    Configurações do admin do model Category
    """
    fields = ('name', 'description', ) # colunas exibidas no formulario do admin
    list_display = ('name', 'get_created_at', 'updated_at', ) # Colunas listadas no admin

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M:%S")
    get_created_at.short_description = "Criado em"



class PostAdmin(admin.ModelAdmin):
    """
    Configurações do admin do model Post
    """
    fields = ('title', 'content', 'category', ) # colunas exibidas no formulario do admin
    list_display = ('title', 'category', 'get_created_at', 'updated_at', ) # Colunas listadas no admin

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M:%S")
    get_created_at.short_description = "Criado em"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
