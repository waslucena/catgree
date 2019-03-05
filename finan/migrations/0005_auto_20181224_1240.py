# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-24 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finan', '0004_auto_20171116_1432'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contacontabil',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='contacontabil',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='contacontabil',
            name='planodecontas',
        ),
        migrations.RemoveField(
            model_name='planodecontas',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='planodecontas',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='ContaContabil',
        ),
        migrations.DeleteModel(
            name='PlanoDeContas',
        ),
    ]