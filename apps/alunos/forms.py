from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        exclude = ('user', 'created_on' , 'updated_on',)