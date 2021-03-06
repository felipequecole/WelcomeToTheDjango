# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20170123_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name': 'aluno', 'verbose_name_plural': 'alunos'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1, verbose_name='sexo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
    ]
