from common.models import SIM_NAO_C
from django.conf import settings
from django.db import models
from model_utils import Choices
from model_utils.fields import AutoCreatedField, AutoLastModifiedField, StatusField

from cliente.models import Pessoa

# Create your models here.

CATEGORIA_CHOICES = (
    ('0', u'Sem Categoria'),
    ('1', u'Categoria 1'),
    ('2', u'Categoria 2'),
    ('3', u'Categoria 3'),
    ('4', u'Categoria 4'),
)


# class hystory(models.Model):
#     tstamp timestamp DEFAULT now(),
#     schemaname text,
#     tabname text,
#     operation text,
#     who text DEFAULT current_user,
#     new_val json,
#     old_val json

# class Cor(models.Model):
#     """
#     Cor
#     """
#     codigo = models.CharField(max_length=1, verbose_name=u'Código FIFe', primary_key=True, default='')
#     nome = models.CharField(max_length=30, verbose_name=u'Nome', default='')
#     descricao = models.CharField(max_length=120, verbose_name=u'Descrição', default='')
#
#     class Meta:
#         verbose_name = u'Cor'
#         verbose_name_plural = u'Cores'
#         ordering = ('nome',)
#
#     def __str__(self):
#         return '%s - %s' % (self.codigo, self.nome)
#
#
# class Cor_Olhos(models.Model):
#     """
#     Cor_Olhos
#     """
#     codigo = models.CharField(max_length=2, verbose_name=u'Código FIFe', primary_key=True, default='')
#     nome = models.CharField(max_length=30, verbose_name=u'Nome', default='')
#     descricao = models.CharField(max_length=120, verbose_name=u'Descrição', default='')
#
#     class Meta:
#         verbose_name = u'Cor dos Olhos'
#         verbose_name_plural = u'Cores dos Olhos'
#         ordering = ('nome',)
#
#     def __str__(self):
#         return '%s - %s' % (self.codigo, self.nome)
#
#
# class Cor_Complementar(models.Model):
#     """
#     Cor_Complementar
#     """
#     codigo = models.CharField(max_length=2, verbose_name=u'Código FIFe', primary_key=True, default='')
#     nome = models.CharField(max_length=30, verbose_name=u'Nome', default='')
#     descricao = models.CharField(max_length=120, verbose_name=u'Descrição', default='')
#
#     class Meta:
#         verbose_name = u'Cor Complementar'
#         verbose_name_plural = u'Cores Complementares'
#         ordering = ('nome',)
#
#     def __str__(self):
#         return '%s - %s' % (self.codigo, self.nome)


class Gatil(models.Model):
    """
    Gatil
    """
    nome = models.CharField(max_length=30, verbose_name=u'Nome', default='')
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name='Proprietário')

    class Meta:
        verbose_name = u'Gatil'
        verbose_name_plural = u'Gatis'
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Raca(models.Model):
    """
    Raca
    """
    ems = models.CharField(max_length=3, verbose_name=u'Código EMS', primary_key=True, default='')
    nome = models.CharField(max_length=50, verbose_name=u'Raça', default='')
    descricao = models.CharField(max_length=120, verbose_name=u'Descrição', default='', null=True)
    raca_irma = models.CharField(max_length=30, verbose_name=u'Raça Irmã', default='', null=True)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, verbose_name='Categoria', default='4',
                                 null=True, help_text='Categoria da raça')
    reconhecida = models.CharField(max_length=1, choices=SIM_NAO_C, verbose_name='Raça Reconhecida', default='S',
                                   help_text='Se a raça é reconhecida ou não')

    class Meta:
        verbose_name = u'Raça'
        verbose_name_plural = u'Raças'
        ordering = ('ems',)

    def __str__(self):
        return '%s' % (self.nome)


class Regra(models.Model):
    """
    Regra
    """
    # codigo = models.CharField(max_length=3, verbose_name=u'Código EMS', primary_key=True, default='')
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name='Raça')
    regra = models.CharField(max_length=30, verbose_name=u'Regra', default='')
    descricao = models.CharField(max_length=120, verbose_name=u'Descrição', default='')

    class Meta:
        verbose_name = u'Regra de Cor'
        verbose_name_plural = u'Regras de Cor'
        unique_together = (('raca', 'regra', 'descricao'),)
        ordering = ('raca', 'regra', 'descricao')

    def __str__(self):
        return '%s - %s' % (self.regra, self.descricao)


class Gato(models.Model):
    """
    Gato
    """
    STATUS = Choices('Em cadastro', 'Pendente', 'Habilitado', 'Inativo')

    SEXO_CHOICES = (
        ('F', 'Fêmea'),
        ('M', 'Macho'),
    )

    # Pais: pai e mae
    # Raça: raca
    # Exame
    # Cor: analise de risco: cor
    # Clube: não tem clube, só gatil
    # Status: status: Habilitado / com risco / pendente
    # Histórico de registros
    # Histórico de donos: Proprietario
    # Títulos de competições? SIM
    # Fotos? NAO
    nome = models.CharField(max_length=100, verbose_name=u'Nome', default='')
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name='Raça')
    cor = models.ForeignKey(Regra, on_delete=models.PROTECT, verbose_name='Cor')
    pai = models.ForeignKey("Gato", on_delete=models.PROTECT, related_name='gato_pai', verbose_name='Pai', blank=True,
                            null=True)
    mae = models.ForeignKey("Gato", on_delete=models.PROTECT, related_name='gata_mae', verbose_name='Mãe', blank=True,
                            null=True)
    gatil = models.ForeignKey(Gatil, on_delete=models.PROTECT, verbose_name='Gatil', blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo', default='F', blank=False,
                            null=False, help_text='Sexo')
    status = StatusField(choices_name='STATUS')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='gato_created_by',
                                   blank=True, null=True, verbose_name=u'Cadastrado Por')
    created_at = AutoCreatedField(verbose_name='Data de Criação')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='gato_modified_by',
                                    blank=True, null=True, verbose_name=u'Modificado Por')
    modified_at = AutoLastModifiedField(verbose_name='Última Modificação')

    class Meta:
        verbose_name = u'Gato'
        verbose_name_plural = u'Gato'
        # unique_together = (('raca', 'regra', 'descricao'),)
        ordering = ('raca', 'cor', 'nome')

    def __str__(self):
        return '%s - %s - %s - %s' % (self.nome, self.raca, self.cor, self.gatil)


class Proprietario(models.Model):
    """
    Relação Gato x Proprietario
    """
    # codigo = models.CharField(max_length=3, verbose_name=u'Código EMS', primary_key=True, default='')
    gato = models.ForeignKey(Gato, on_delete=models.PROTECT, verbose_name='Gato')
    proprietario = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name='Proprietário')
    dataini = models.DateField(blank=False, null=False, verbose_name='Data Início Propriedade')
    datafin = models.DateField(blank=True, null=True, verbose_name='Data Término Propriedade')

    class Meta:
        verbose_name = u'Proprietário'
        verbose_name_plural = u'Proprietários'
        unique_together = (('gato', 'proprietario',),)
        ordering = ('gato', 'proprietario', 'dataini',)

    def __str__(self):
        return '%s - %s' % (self.proprietario, self.dataini)


class Documento(models.Model):
    """
    Documento
    """
    descricao = models.CharField(max_length=255, blank=True, verbose_name='Descrição', default='')
    documento = models.FileField(upload_to='documentos/')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True,
                                   related_name='documento_created_by', verbose_name=u'Cadastrado Por')
    created_at = AutoCreatedField(verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        # ordering = ('gato', 'proprietario', 'dataini',)

    def __str__(self):
        return '%s - %s' % (self.descricao, self.descricao)


class Gato_Documento(models.Model):
    """
    Relação Gato x Documento
    """
    gato = models.ForeignKey(Gato, on_delete=models.PROTECT, verbose_name='Gato')
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT, verbose_name='Documento')

    class Meta:
        verbose_name = 'Gato_Documento'
        verbose_name_plural = 'Gato_Documentos'
        unique_together = (('gato', 'documento',),)
        ordering = ('gato', 'documento',)

    def __str__(self):
        return '%s - %s' % (self.gato, self.documento)
