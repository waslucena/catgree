# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-25 15:31
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0020_ninhada_outcross'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninhada',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='R', max_length=100, no_check_for_status=True),
        ),
    ]