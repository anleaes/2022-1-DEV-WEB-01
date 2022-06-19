from django import forms
from .models import Matricula, Aluno, MatriculaItem ,Disciplina

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        exclude = ('user', 'aluno', 'created_on' , 'updated_on',)

class MatriculaItemForm(forms.ModelForm):
    
    class Meta:
        model = MatriculaItem
        exclude = ('user', 'matricula', 'created_on' , 'updated_on',)
