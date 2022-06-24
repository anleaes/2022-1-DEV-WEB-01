# Generated by Django 3.2.5 on 2022-06-24 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Preco Total')),
                ('status', models.CharField(blank=True, choices=[('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], default='Em andamento', max_length=20, null=True, verbose_name='Status')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.aluno')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='MatriculaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('unitary_price', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Preco unitario')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplinas.disciplina')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculas.matricula')),
            ],
            options={
                'verbose_name': 'Item de pedido',
                'verbose_name_plural': 'Itens de pedido',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='matricula',
            name='matricula_item',
            field=models.ManyToManyField(blank=True, through='matriculas.MatriculaItem', to='disciplinas.Disciplina'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
