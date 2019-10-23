import reversion
from common.fields import validateDateLTEToday
from common.models import SIM_NAO_C, UserAudit
from django.core.exceptions import ValidationError
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from cliente.models import Pessoa

# Create your models here.

CATEGORIA_CHOICES = (
    ('0', u'Sem Categoria'),
    ('1', u'Categoria 1'),
    ('2', u'Categoria 2'),
    ('3', u'Categoria 3'),
    ('4', u'Categoria 4'),
)


@reversion.register()
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


@reversion.register()
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


@reversion.register()
class Ninhada(UserAudit):
    """
    Ninhada
    """
    STATUS = Choices(('1', 'Em cadastro'),
                     ('2', 'Pendente'),
                     ('3', 'Habilitado'),
                     ('4', 'Homologado'),
                     ('5', 'Inativo'))

    datanasc = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    gatil = models.ForeignKey(Gatil, on_delete=models.PROTECT, verbose_name='Gatil', blank=True, null=True)
    outcross = models.CharField(max_length=1, choices=SIM_NAO_C, verbose_name='Outcross', default='N',
                                help_text='Se o cruzamento é com raças não autorizadas.')
    qtde = models.IntegerField(verbose_name='Quantidade de filhotes', null=True)
    pai = models.ForeignKey('Gato', on_delete=models.PROTECT, related_name='ninhada_pai', verbose_name='Pai',
                            blank=False, null=False)
    mae = models.ForeignKey('Gato', on_delete=models.PROTECT, related_name='ninhada_mae', verbose_name='Mãe',
                            blank=False, null=False)
    status = StatusField(choices_name='STATUS', default='R')

    class Meta:
        verbose_name = 'Ninhada'
        verbose_name_plural = 'Ninhadas'
        unique_together = (('pai', 'mae', 'datanasc'),)
        # ordering = ('gato', 'documento',)

    def __str__(self):
        return '%s - %s' % (self.pai, self.mae)

@reversion.register()
class Gato(UserAudit):
    """
    Gato
    """

    STATUS = Ninhada.STATUS

    LO_RX = Choices(('R', 'RX'),
                    ('L', 'LO'), )

    SEXO_CHOICES = Choices(
        ('F', 'Fêmea'),
        ('M', 'Macho'),
    )

    ninhada = models.ForeignKey(Ninhada, on_delete=models.PROTECT, verbose_name='Ninhada', blank=True, null=True)

    nome = models.CharField(max_length=100, verbose_name='Nome', default='')
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name='Raça')
    cor = models.ForeignKey(Regra, on_delete=models.PROTECT, verbose_name='Cor')
    pai = models.ForeignKey("Gato", on_delete=models.PROTECT, related_name='gato_pai', verbose_name='Pai', blank=True,
                            null=True)
    mae = models.ForeignKey("Gato", on_delete=models.PROTECT, related_name='gata_mae', verbose_name='Mãe', blank=True,
                            null=True)
    gatil = models.ForeignKey(Gatil, on_delete=models.PROTECT, verbose_name='Gatil', blank=True, null=True)
    sexo = StatusField(choices_name='SEXO_CHOICES', verbose_name='Sexo', default='F', blank=False, null=False)
    outcross = models.CharField(max_length=1, choices=SIM_NAO_C, verbose_name='Outcross', default='N',
                                help_text='Se o cruzamento é com raças não autorizadas.')

    microchip = models.CharField(max_length=15, verbose_name='Microchip', blank=True, null=True, unique=True,
                                 help_text='O número de microchip é obrigatório para todos os gatos que estão sendo usados para reprodução, desta forma pai e mãe de cada ninhada devem ter obrigatoriamente número de microchip.')
    lo_rx = StatusField(choices_name='LO_RX', verbose_name='LO/RX', default='R')
    pedigree_anterior = models.CharField(max_length=15, verbose_name='Pedigree Anterior', blank=True, null=True,
                                         default='',
                                         help_text='Pedigree anterior se o gato veio de outra federação ou é estrangeiro.')
    breeding = models.CharField(max_length=1, choices=SIM_NAO_C, verbose_name='Para Reprodução', default='S',
                                help_text='Informe se se destina ou não a criação, essa informação estará presente no pedigree impresso.')
    breeding_able = models.CharField(max_length=1, choices=SIM_NAO_C, verbose_name='Apto para Reprodução', default='N',
                                     help_text='Se está apto para reprodução ou não.')
    breeding_able_date = models.DateField(blank=True, null=True, verbose_name='Data documento',
                                          validators=[validateDateLTEToday],
                                          help_text='Se está apto para reprodução, é obrigatório informar a data de emissão do documento comprobatório.')

    status = StatusField(choices_name='STATUS')

    class Meta:
        verbose_name = u'Gato'
        verbose_name_plural = u'Gato'
        # unique_together = (('raca', 'regra', 'descricao'),)
        ordering = ('raca', 'cor', 'nome')

    @property
    def pedigree(self):
        return 'BR FFB {0:2s} {1:0=6d}'.format(self.LO_RX[self.lo_rx], self.id)

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.pedigree, self.nome, self.raca, self.cor, self.gatil)

    def clean_fields(self, exclude=None):
        # Crítica de não ser nem o próprio pai nem a própria mãe
        if self.pai and self.id == self.pai.id:
            raise ValidationError({'pai': "O pai não pode ser o próprio gato!"})
        if self.mae and self.id == self.mae.id:
            raise ValidationError({'mae': "A mãe não pode ser a própria gata!"})

        # Crítica de que a raca do gato tem que ser a mesma dos pais ou de raças irmãs das dos pais
        if hasattr(self, 'raca') and self.raca:
            racas = (self.raca.ems + ((',' + self.raca.raca_irma) if self.raca.raca_irma else '')).replace(' ', '')
            racas = racas.split(',')
            if self.pai and self.pai.raca_id not in racas and self.outcross == 'N':
                raise ValidationError({'pai': "A pai tem que ser da mesma raça do gato ou de raças irmãs !"})
            if self.mae and self.mae.raca_id not in racas and self.outcross == 'N':
                raise ValidationError({'mae': "A mãe tem que ser da mesma raça do gato ou de raças irmãs !"})
        else:
            raise ValidationError({'raca': 'Raça é obrigatória.'})

        # Crítica da cor valida para a raça
        if not self.cor or self.cor.raca != self.raca:
            raise ValidationError({'cor': "Cor selecionada não é válida para a raça escolhida !"})

        # # Outcross não pode ser breeding
        # if self.outcross == 'S' and self.breeding == 'S':
        #     raise ValidationError({'breeding': "Outcross não pode ser para reprodução !"})

        # Breeding
        if self.breeding == 'S':
            # Breeding tem que ter microchip
            if not self.microchip or len(self.microchip) != 15:
                raise ValidationError({
                    'microchip': "Se está apto para reprodução, então tem que ter microchip e o tamanho do código deve ser 15 !"})

            # Breeding: pais tem que ser cadastrados
            if not self.pai:
                raise ValidationError({
                    'pai': "Se está apto para reprodução, então tem que ter pai !"})
            if not self.mae:
                raise ValidationError({
                    'mae': "Se está apto para reprodução, então tem que ter mãe !"})

            # Breeding pais tem que ter microchip
            if not self.pai.microchip:
                raise ValidationError({
                    'pai': "Se está apto para reprodução, então tem o pai que ter microchip !"})
            if not self.mae.microchip:
                raise ValidationError({
                    'mae': "Se está apto para reprodução, então tem a mãe que ter microchip !"})

            # Breeding able tem que ter data do certificado
            if not self.breeding_able_date:
                raise ValidationError({
                    'breeding_able_date': "Se está apto para reprodução, então tem que ser preenchida a data do certificado comprobatório !"})

        return super().clean_fields(exclude=exclude)

    def save(self, *args, **kwargs):
        # Quando vem de ninhada os campos de pai, mãe e gatil estão hidden e não são preenchidos
        # Mas é pra ser aqui ou no clean?
        if self.ninhada and not self.pai:
            self.pai = self.ninhada.pai

        if self.ninhada and not self.mae:
            self.mae = self.ninhada.mae

        if self.ninhada and not self.gatil:
            self.gatil = self.ninhada.gatil

        super().save(*args, **kwargs)


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


class Documento(UserAudit):
    """
    Documento
    """
    descricao = models.CharField(max_length=255, blank=True, verbose_name='Descrição', default='')
    documento = models.FileField(upload_to='documentos/')

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
        verbose_name = 'Documento do Gato'
        verbose_name_plural = 'Documentos do Gato'
        unique_together = (('gato', 'documento',),)
        ordering = ('gato', 'documento',)

    def __str__(self):
        return '%s - %s' % (self.gato, self.documento)


