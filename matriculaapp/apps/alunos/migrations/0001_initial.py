# Generated by Django 3.2.5 on 2022-06-19 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('address', models.CharField(max_length=200, verbose_name='Endereco')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Genero')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['id'],
            },
        ),
    ]
