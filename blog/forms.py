#-*- coding: utf-8 -*-
from django import forms

from blog.models import Category

#6 - ModelForm completo
class CategoryForm(forms.ModelForm):
    
    #created_at = forms.CharField(label='Cadastrado em', widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = Category
        fields = '__all__'
        #exclude = ('created_at', 'updated_at')

    def clean(self):
        super(CategoryForm, self).clean()

        if not self.cleaned_data.get('name') and not self.cleaned_data.get('description'):
            raise forms.ValidationError("Informe nome e descrição.")
        return self.cleaned_data
