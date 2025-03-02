from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'sinopse', 'genero', 'duracao', 'diretor', 'ano', 'faixa_etaria']
        