# -*- coding: utf-8 -*-

import common.models as common
from django.conf import settings
from django.db import models


from cliente import models as cliente_models

# ALUGAR_FLOWS = {
#     # 'contratoadm': [{'pk': 5, 'key': 'Contrato Adm Simples', 'descr': 'Contrato de Administração Simples'},
#     #                 {'pk': 3, 'key': 'Atendimento', 'descr': 'Contrato de Administração Completo'}, ],
#     # 'contratoloc': [{'pk': 5, 'key': 'Contrato Loc Simples', 'descr': 'Contrato de Locação Simples'},
#     #                 {'pk': 3, 'key': 'Atendimento', 'descr': 'Contrato de Locação Completo'}, ],
#     # 'atendimento': [{'pk': 1, 'key': 'Atendimento', 'descr': 'Atendimento de Manutenção'}, ],
#     'contratoadm': [{'pk': '5', 'key': 'Contrato Adm Simples', 'descr': 'Contrato de Administração Simples'},
#                     {'pk': '3', 'key': 'Dúvida Simples', 'descr': 'Contrato de Administração Completo'}, ],
#     'contratoloc': [{'pk': '6', 'key': 'Contrato Loc Simples', 'descr': 'Contrato de Locação Simples'},
#                     {'pk': '3', 'key': 'Dúvida Simples', 'descr': 'Contrato de Locação Completo'}, ],
#     'atendimento': [{'pk': '1', 'key': 'Atendimento', 'descr': 'Atendimento de Manutenção'},
#                     {'pk': '3', 'key': 'Dúvida Simples', 'descr': 'Contrato de Locação Completo'}, ],
# }
#
# ALUGAR_FLOW_CONTRATO_ADM_CHOICES = tuple([(x['pk'], x['descr']) for x in ALUGAR_FLOWS['contratoadm']])
# ALUGAR_FLOW_CONTRATO_LOC_CHOICES = tuple([(x['pk'], x['descr']) for x in ALUGAR_FLOWS['contratoloc']])


class Configuracao(common.Configuracao):
    """
    Configuração
    """
    # apelido = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name=u'Apelido', default='')
    # Pessoa Jurídica associada a empresa
    empresa = models.ForeignKey(cliente_models.PessoaJuridica, on_delete=models.PROTECT, verbose_name=u'Empresa')

    class Meta:
        verbose_name = u'Configuracao'
        verbose_name_plural = u'Configurações'
        ordering = ('apelido',)
        # managed = False

    def __str__(self):
        return u'%s' % self.apelido


try:
    empresa = Configuracao.objects.get(pk=settings.EMPRESA_CORRENTE)
except Exception as v:
    # from finan.models import PlanoDeContas

    empresa = Configuracao()
    # try:
    #     empresa.planodecontas = PlanoDeContas.objects.get(pk=settings.PLANO_DE_CONTA_CORRENTE)
    # except:
    #     pass
