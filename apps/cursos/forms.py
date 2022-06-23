from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        exclude = ('created_on' , 'updated_on',)
