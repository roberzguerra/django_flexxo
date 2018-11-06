# -*- coding: utf-8 -*-

from django.db import models

class Category(models.Model):
    """
    Model para as categorias do blog
    """
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Nome")
    description = models.TextField(blank=False, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Alterado em")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    
class Post(models.Model):
    """
    Model para os posts do blog
    """
    title = models.CharField(verbose_name="Título", max_length=255, blank=False, null=False)
    content = models.TextField(verbose_name="Conteúdo", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Alterado em")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"