from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Areadeconhecimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=1000) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Área de Conhecimento'
        verbose_name_plural = 'Áreas de Conhecimento'
        ordering =['id']

    def __str__(self):
        return self.name