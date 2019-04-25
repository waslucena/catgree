# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 18:55
from __future__ import unicode_literals

import common.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_auto_20180405_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='modified_at',
            field=common.fields.AutoModifiedAtField(default=django.utils.timezone.now, verbose_name='Última Modificação'),
        ),
    ]