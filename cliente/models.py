# -*- coding: utf-8 -*-



import itertools

from django.conf import settings
from django.core import validators
from django.core.validators import EmailValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

import common.fields as common_fields
from model_utils.fields import AutoLastModifiedField, AutoCreatedField

from cliente.fields import MunicipioForeignKey
from common import models as common_models
from common.utils import validate_cpf, validate_cnpj
from finan.models import Banco


# Create your models here.


class Estado(models.Model):
    """
    Estados
    """
    sigla = models.CharField(max_length=2, verbose_name='Sigla', primary_key=True, default='')
    estado = models.CharField(max_length=20, verbose_name='Estado', default='')
    ibge = models.CharField(max_length=2, verbose_name='Código IBGE', default='', help_text='Código IBGE do Estado')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ('sigla', 'estado')
        # managed = False
        # db_table = 'estado'
        # app_label = 'cliente'

    def __str__(self):
        return '%s' % self.estado


class Municipio(models.Model):
    """
    Municípios
    """
    ibge = models.CharField(max_length=7, primary_key=True, verbose_name='Código IBGE', default='',
                            help_text='Código IBGE do Município')
    nome = models.CharField(max_length=60, verbose_name='Município', default='')
    uf = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name='Estado')

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ('uf', 'nome')
        # managed = False
        # db_table = 'municipio'
        # app_label = 'cliente'

    def __str__(self):
        return '%s - %s' % (self.nome, self.uf)


class CEP(models.Model):
    """
    CEP
    """
    cep = models.CharField(max_length=10, primary_key=True, verbose_name='CEP', default='')
    endereco = models.CharField(max_length=60, verbose_name='Endereço', default='',
                                help_text='Logradouro conforme Correios')
    # complemento = models.CharField(max_length=60, verbose_name='Complemento', default='', blank=True, null=True)
    # Lado par, de número X a Y
    bairro = models.CharField(max_length=60, default='', help_text='Bairro conforme Correios')
    # localidade = models.CharField(max_length=60, default='', help_text='Localidade conforme Correios')
    municipio = MunicipioForeignKey(Municipio, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'CEP'
        verbose_name_plural = 'CEPs'
        ordering = ('cep', 'estado')
        # managed = False
        # db_table = 'municipio'
        # app_label = 'cliente'

    def __str__(self):
        return '%s' % self.cep


class Pessoa(models.Model):
    # Constantes do módulo
    TIPO_PESSOA_C = (('F', u'Pessoa Física'), ('J', u'Pessoa Jurídica'))

    # Tipo de Pessoa
    DEFAULT_TIPO = 'P'

    nome = models.CharField(max_length=80, default='')
    email = models.EmailField(max_length=80, blank=True, null=True, verbose_name=u'Email de Contato', default='',
                              help_text=u'eMail de contato',
                              validators=[EmailValidator(message='Entre um endereço de eMail válido')])
    emailnf = models.EmailField(max_length=254, blank=True, null=True, verbose_name=u'Email da NFe', default='',
                                help_text=u'eMail de recebimento de NFe',
                                validators=[EmailValidator(message='Entre um endereço de eMail válido')])
    msg = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Mensagem', default='')
    telefone = models.CharField(max_length=15, blank=True, null=True, default='', help_text=u'Formato: (99) 9999-9999')
    celular = models.CharField(max_length=15, blank=True, null=True, default='', help_text=u'Formato: (99) 99999-9999')
    ativo = models.CharField(max_length=1, null=True, blank=True, verbose_name=u'Status', default='S',
                             choices=common_models.ATIVO_C)
    usuariointernet = models.CharField(max_length=20, blank=True, null=True, default='',
                                       verbose_name=u'Usuario Internet')
    senhainternet = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name=u'Senha Internet')

    endereco = models.CharField(max_length=60, verbose_name=u'Endereço', default='',
                                help_text=u'Preencha sem abreviações. Ex: Rua Lobo Júnior')
    enderecoNumero = models.CharField(max_length=10, verbose_name=u'Número', default='',
                                      help_text=u'Ou \'S/N\' se não existir')
    complemento = models.CharField(max_length=60, verbose_name=u'Complemento', default='', blank=True, null=True)
    bairro = models.CharField(max_length=60, default='', help_text=u'Preencha sem abreviações. Ex: Penha')
    municipio = MunicipioForeignKey(Municipio, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    cep = models.CharField(max_length=10, verbose_name='CEP', default='', help_text=u'Ex.: 21020-122')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='pessoa_created_by',
                                   blank=True, null=True, verbose_name=u'Cadastrado Por')
    created_at = common_fields.AutoCreatedAtField(verbose_name=u'Data de Criação')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                    related_name='pessoa_modified_by', blank=True, null=True,
                                    verbose_name=u'Modificado Por')
    modified_at = common_fields.AutoModifiedAtField(verbose_name='Última Modificação')

    tipo = models.CharField(max_length=1, null=True, blank=True, verbose_name='Tipo de Pessoa', default=DEFAULT_TIPO,
                            choices=TIPO_PESSOA_C, editable=False)

    slug = models.SlugField(max_length=100, default='1', null=True, blank=True)

    # slug = models.SlugField(max_length=100, unique=True, validators=[validate_pessoa_slug], default='1')

    class Meta:
        verbose_name = u'Pessoa'
        verbose_name_plural = u'Pessoas'
        ordering = ('nome',)

    def __str__(self):
        if self.tipo == 'F':
            pf = PessoaFisica.objects.get(pk=self.id)
            return pf.__str__()
        if self.tipo == 'J':
            pf = PessoaJuridica.objects.get(pk=self.id)
            return pf.__str__()

        return u"%s - %s" % (self.id, self.nome)

    def get_absolute_url(self):
        return reverse('cliente:pessoa', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_by = self.modified_by

        # Newly created object, so set slug
        # Atualiza slug se tipo = Pessoa
        if self.tipo == Pessoa.DEFAULT_TIPO:
            self.slug = 'p-%s' % self.nome
        novo_slug = orig_slug = slugify(self.slug)
        for x in itertools.count(1):
            if not Pessoa.objects.filter(slug=novo_slug).exists():
                break
            else:
                novo_slug = '%s-%d' % (orig_slug, x)
        self.slug = novo_slug
        super().save(*args, **kwargs)


class PessoaFisica(Pessoa):
    # Tipo de Pessoa
    DEFAULT_TIPO = 'F'

    cpf = models.CharField(max_length=14, validators=[validate_cpf])
    rg = models.CharField(max_length=12, blank=True, null=True, default='')
    orgaoexpedidor = models.CharField(max_length=6, blank=True, null=True, default='', verbose_name='Órgão Expedidor')
    dataexp = models.DateField(blank=True, null=True, verbose_name='Data Expedição')
    sexo = models.CharField(max_length=1, blank=True, null=True, choices=common_models.SEXO_C)
    datanascimento = models.DateField(blank=True, null=True, verbose_name='Nascimento', )
    estadocivil = models.CharField(max_length=1, blank=True, null=True, default='C', verbose_name='Estado Civil',
                                   choices=common_models.ESTADOCIVIL_C)
    nacionalidade = models.CharField(max_length=20, blank=True, null=True, default='')
    naturalidade = models.CharField(max_length=40, blank=True, null=True, default='')
    pai = models.CharField(max_length=40, blank=True, null=True, default='')
    mae = models.CharField(max_length=40, blank=True, null=True, verbose_name='Mãe', default='')
    passaporte = models.CharField(max_length=30, blank=True, null=True, default='')

    class Meta:
        verbose_name = u'Pessoa Física'
        verbose_name_plural = u'Pessoas Físicas'

    def get_absolute_url(self):
        return reverse('cliente:pessoafisica', args=[self.slug])

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        # Atualiza slug, o tratamento de duplicidade é na Pessoa
        self.slug = 'f-%s-%s' % (self.cpf, self.nome)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = self.DEFAULT_TIPO

    def __str__(self):
        return u"%s - %s - %s" % (self.id, self.nome, self.cpf)


class PessoaJuridica(Pessoa):
    # Tipo de Pessoa
    DEFAULT_TIPO = 'J'

    cnpj = models.CharField(max_length=18, validators=[validate_cnpj])
    contato = models.CharField(max_length=80, blank=True, null=True, default='')
    nrinscrmunicip = models.CharField(max_length=15, blank=True, null=True, default='',
                                      verbose_name='Inscrição Municipal')
    nrinscrestadual = models.CharField(max_length=15, blank=True, null=True, default='',
                                       verbose_name='Inscrição Estadual')

    def get_absolute_url(self):
        return reverse('cliente:pessoajuridica', args=[self.slug])

    class Meta:
        verbose_name = u'Pessoa Jurídica'
        verbose_name_plural = u'Pessoas Jurídicas'

    def save(self, *args, **kwargs):
        self.slug = 'j-%s-%s' % (self.cnpj, self.nome)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = self.DEFAULT_TIPO

    def __str__(self):
        return u"%s - %s - %s" % (self.id, self.nome, self.cnpj)


class ContaBancaria(models.Model):
    """
    Conta Bancária de Pessoa
    """
    CONTA_BANCARIA_TIPO_CORRENTE = '1'
    CONTA_BANCARIA_TIPO_POUPANCA = '2'
    CONTA_BANCARIA_TIPO_INVESTIMENTO = '3'
    CONTA_BANCARIA_TIPO_OUTRO = '4'

    CONTA_BANCARIA_TIPO = (
        (CONTA_BANCARIA_TIPO_CORRENTE, 'Corrente'),
        (CONTA_BANCARIA_TIPO_POUPANCA, 'Poupança'),
        (CONTA_BANCARIA_TIPO_INVESTIMENTO, 'Investimento'),
        (CONTA_BANCARIA_TIPO_OUTRO, 'Outro'),
    )

    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    agencia = models.PositiveSmallIntegerField(blank=False, null=False,
                                               validators=[validators.MinValueValidator(1),
                                                           validators.MaxValueValidator(9999)], default=0,
                                               verbose_name='Agência',
                                               help_text='Agência bancária sem DV')
    agencia_dv = models.CharField(max_length=2, blank=True, null=False, verbose_name='DV Agência',
                                  default='', help_text='DV da agência bancária')
    conta = models.DecimalField(max_digits=13, decimal_places=0,
                                validators=[validators.MinValueValidator(1),
                                            validators.MaxValueValidator(9999999999999)],
                                blank=False, null=False, default=0, verbose_name='Conta',
                                help_text='Número da conta sem DV')
    conta_dv = models.CharField(max_length=2, blank=True, null=False, verbose_name='DV Conta',
                                default='', help_text='DV da conta corrente')
    tipo_conta = models.CharField(max_length=1, blank=True, null=False, verbose_name='Tipo de Conta',
                                  default=CONTA_BANCARIA_TIPO_CORRENTE, choices=CONTA_BANCARIA_TIPO)

    ativo = models.CharField(max_length=1, null=True, blank=True, verbose_name=u'Status', default='S',
                             choices=common_models.ATIVO_C)

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'
        ordering = ('banco', 'agencia')
        # managed = False
        # db_table = 'municipio'
        # app_label = 'cliente'

    def __str__(self):
        return '%s / %s-%s / %s-%s' % (self.banco.nome, self.agencia, self.agencia_dv, self.conta, self.conta_dv)

# from generic_scaffold import CrudManager


# class MunicipioCrudManager(CrudManager):
#     model = Municipio
#     prefix = 'municipio'
