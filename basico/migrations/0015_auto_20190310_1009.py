# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 13:09
from __future__ import unicode_literals

import common.fields
from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basico', '0014_auto_20190308_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ninhada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Ninhada',
                'verbose_name_plural': 'Ninhadas',
            },
        ),
        migrations.AlterModelOptions(
            name='gato_documento',
            options={'ordering': ('gato', 'documento'), 'verbose_name': 'Documento do Gato', 'verbose_name_plural': 'Documentos do Gato'},
        ),
        migrations.AlterField(
            model_name='gato',
            name='breeding',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', help_text='Informe se se destina ou não a criação, essa informação estará presente no pedigree impresso.', max_length=1, verbose_name='Para Reprodução'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='breeding_able_date',
            field=models.DateField(blank=True, help_text='Se está apto para reprodução, é obrigatório informar a data de emissão do documento comprobatório.', null=True, validators=[common.fields.validateDateLTEToday], verbose_name='Data documento'),
        ),
        migrations.AlterField(
            model_name='gato',
            name='lo_rx',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='R', max_length=100, no_check_for_status=True, verbose_name='LO/RX'),
        ),
        migrations.AddField(
            model_name='ninhada',
            name='mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ninhada_mae', to='basico.Gato', verbose_name='Mãe'),
        ),
        migrations.AddField(
            model_name='ninhada',
            name='pai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ninhada_pai', to='basico.Gato', verbose_name='Pai'),
        ),
    ]
