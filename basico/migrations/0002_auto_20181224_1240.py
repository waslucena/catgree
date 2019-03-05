# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-24 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regra', models.CharField(default='', max_length=30, unique=True, verbose_name='Regra')),
                ('descricao', models.CharField(default='', max_length=120, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Regra de Cor',
                'ordering': ('regra',),
                'verbose_name_plural': 'Regras de Cor',
            },
        ),
        migrations.AlterModelOptions(
            name='raca',
            options={'ordering': ('ems',), 'verbose_name': 'Raça', 'verbose_name_plural': 'Raças'},
        ),
    ]
