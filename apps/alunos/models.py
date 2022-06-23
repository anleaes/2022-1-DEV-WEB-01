from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aluno(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering =['id']

    def __str__(self):
        return self.first_name