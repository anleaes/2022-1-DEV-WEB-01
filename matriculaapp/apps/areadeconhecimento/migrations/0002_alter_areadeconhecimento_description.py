# Generated by Django 3.2.5 on 2022-06-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areadeconhecimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areadeconhecimento',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Descricao'),
        ),
    ]