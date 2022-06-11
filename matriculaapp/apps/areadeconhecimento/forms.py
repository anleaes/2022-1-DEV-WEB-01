from django import forms
from .models import Areadeconhecimento

class AreadeconhecimentoForm(forms.ModelForm):

    class Meta:
        model = Areadeconhecimento
        exclude = ('user', 'created_on' , 'updated_on',)