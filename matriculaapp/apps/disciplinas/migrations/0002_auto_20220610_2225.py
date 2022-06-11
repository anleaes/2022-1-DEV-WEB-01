# Generated by Django 3.2.5 on 2022-06-11 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areadeconhecimento', '0001_initial'),
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaAreadeconhecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('areadeconhecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='areadeconhecimento.areadeconhecimento')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.disciplina')),
            ],
            options={
                'verbose_name': 'Item de Área de Conhecimento',
                'verbose_name_plural': 'Itens de Áreas de Conhecimento',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_areadeconhecimento',
            field=models.ManyToManyField(blank=True, through='disciplinas.DisciplinaAreadeconhecimento', to='areadeconhecimento.Areadeconhecimento'),
        ),
    ]