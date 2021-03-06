# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0013_gato_outcross'),
    ]

    operations = [
        migrations.AddField(
            model_name='gato',
            name='breeding',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Informe se se destina ou não a criação, essa informação estará presente no pedigree impresso.', max_length=1, verbose_name='Para Reprodução'),
        ),
        migrations.AddField(
            model_name='gato',
            name='breeding_able',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Se está apto para reprodução ou não.', max_length=1, verbose_name='Apto para Reprodução'),
        ),
        migrations.AddField(
            model_name='gato',
            name='breeding_able_date',
            field=models.DateField(blank=True, help_text='Se está apto para reprodução, é obrigatório informar a data de emissão do documento comprobatório.', null=True, verbose_name='Data documento comprobatório'),
        ),
        migrations.AddField(
            model_name='gato',
            name='lo_rx',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='L', max_length=100, no_check_for_status=True),
        ),
        migrations.AddField(
            model_name='gato',
            name='microchip',
            field=models.CharField(blank=True, help_text='O número de microchip é obrigatório para todos os gatos que estão sendo usados para reprodução, desta forma pai e mãe de cada ninhada devem ter obrigatoriamente número de microchip.', max_length=15, null=True, unique=True, verbose_name='Microchip'),
        ),
        migrations.AddField(
            model_name='gato',
            name='pedigree_anterior',
            field=models.CharField(blank=True, default='', help_text='Pedigree anterior se o gato veio de outra federação ou é estrangeiro.', max_length=15, null=True, verbose_name='Pedigree Anterior'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='outcross',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', help_text='Se o cruzamento é com raças não autorizadas.', max_length=1, verbose_name='Outcross'),
        ),
    ]
