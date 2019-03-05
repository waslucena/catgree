# -*- coding: utf-8 -*-


from django.db import models
from mptt.models import MPTTModel

# Create your models here.

class Banco(models.Model):
    """
    Banco
    """
    codigoCompensacao = models.CharField(max_length=3, verbose_name=u'Código Compensação', primary_key=True, default='')
    nome = models.CharField(max_length=60, verbose_name=u'Nome', default='')

    class Meta:
        verbose_name = u'Banco'
        verbose_name_plural = u'Bancos'
        ordering = ('nome',)

    def __str__(self):
        return u'%s - %s' % (self.codigoCompensacao, self.nome)


class Indice(models.Model):
    """
    Índice de Correção
    """
    nome = models.CharField(max_length=60, verbose_name=u'Nome', default='')

    class Meta:
        verbose_name = u'Índice de Correção'
        verbose_name_plural = u'Índices de Correção'
        ordering = ('nome',)

    def __str__(self):
        return u'%s - %s' % (self.pk, self.nome)
