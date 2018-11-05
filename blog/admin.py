# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    Configurações do admin do model Category
    """
    fields = ('name', 'description', )
    list_display = ('name', 'get_created_at', 'updated_at', )

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M:%S")
    get_created_at.short_description = "Criado em"


admin.site.register(Category, CategoryAdmin)
