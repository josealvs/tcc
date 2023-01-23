from urllib import request
from django import forms
from .models import projetos, atividades

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = projetos
        fields = {'titulo', 'descricao', 'aluno', 'data_inicio'}

class AtividadeForm (forms.ModelForm):
    class Meta:
        model = atividades
        fields = {'descricao', 'status', 'projeto', 'aluno'}
