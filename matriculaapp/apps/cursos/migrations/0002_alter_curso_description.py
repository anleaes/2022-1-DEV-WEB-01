# Generated by Django 3.2.5 on 2022-06-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Descricao'),
        ),
    ]
