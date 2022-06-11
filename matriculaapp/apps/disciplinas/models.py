from django.db import models
from cursos.models import Curso
from django.contrib.auth.models import User
from areadeconhecimento.models import Areadeconhecimento

# Create your models here.

class Disciplina(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    disciplina_areadeconhecimento = models.ManyToManyField(Areadeconhecimento, through='DisciplinaAreadeconhecimento', blank=True)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name

class DisciplinaAreadeconhecimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    areadeconhecimento = models.ForeignKey(Areadeconhecimento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de Área de Conhecimento'
        verbose_name_plural = 'Itens de Áreas de Conhecimento'
        ordering =['id']

    def __str__(self):
        return self.areadeconhecimento.name        