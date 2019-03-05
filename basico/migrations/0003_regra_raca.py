# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-24 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0002_auto_20181224_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='regra',
            name='raca',
            field=models.ForeignKey(default='TUV', on_delete=django.db.models.deletion.PROTECT, to='basico.Raca', verbose_name='Raça'),
            preserve_default=False,
        ),
    ]
