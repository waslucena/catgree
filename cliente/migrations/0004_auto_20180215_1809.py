# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-15 20:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_contabancaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cep',
            name='cep',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cep',
            name='endereco',
            field=models.CharField(default='', help_text='Logradouro conforme Correios', max_length=70, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(default='', help_text='Ex.: 21020-122', max_length=10, verbose_name='CEP'),
        ),
    ]