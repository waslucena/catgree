# -*- coding: utf-8 -*-
from common.form import CommonModelForm
from common.layout import LabelFirstDetail
from crispy_forms.bootstrap import InlineField
from crispy_forms.layout import Layout, Div, Field, Hidden
from dal import autocomplete, forward
from django import forms
from table import Table
from table.columns import Column, ActionColumn

from .models import *


# class CorForm(CommonModelForm):
#     def layout(self):
#         return Layout(
#             Div('codigo',
#                 'nome',
#                 'descricao',
#                 # css_class='col-md-3'
#                 )
#         )
#
#     class Meta:
#         model = Cor
#         include_hidden = True
#         fields = '__all__'
#         widgets = {
#             'descricao': forms.Textarea(attrs={'rows': 3, }),
#         }
#
#
# class CorTable(Table):
#     """
#     Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
#     """
#     codigo = Column(header=u'Código FIFe', field='codigo')
#     nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
#     # descricao = Column(header=u'Descricao', field='descricao', header_attrs={'width': '60%'})
#     action = ActionColumn(vieweditdelete='corEditDelete', chave='codigo')
#
#     class Meta:
#         model = Cor
#
#
# class CorOlhosForm(CommonModelForm):
#     def layout(self):
#         return Layout(
#             Div('codigo',
#                 'nome',
#                 'descricao',
#                 # css_class='col-md-3'
#                 )
#         )
#
#     class Meta:
#         model = Cor_Olhos
#         include_hidden = True
#         fields = '__all__'
#         widgets = {
#             'descricao': forms.Textarea(attrs={'rows': 3, }),
#         }
#
#
# class CorOlhosTable(Table):
#     """
#     Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
#     """
#     codigo = Column(header=u'Código FIFe', field='codigo')
#     nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
#     # descricao = Column(header=u'Descricao', field='descricao', header_attrs={'width': '60%'})
#     action = ActionColumn(vieweditdelete='cor_olhosEditDelete', chave='codigo')
#
#     class Meta:
#         model = Cor_Olhos
#
#
# class CorComplementarForm(CommonModelForm):
#     def layout(self):
#         return Layout(
#             Div('codigo',
#                 'nome',
#                 'descricao',
#                 # css_class='col-md-3'
#                 )
#         )
#
#     class Meta:
#         model = Cor_Complementar
#         include_hidden = True
#         fields = '__all__'
#         widgets = {
#             'descricao': forms.Textarea(attrs={'rows': 3, }),
#         }
#
#
# class CorComplementarTable(Table):
#     """
#     Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
#     """
#     codigo = Column(header=u'Código FIFe', field='codigo')
#     nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
#     # descricao = Column(header=u'Descricao', field='descricao', header_attrs={'width': '60%'})
#     action = ActionColumn(vieweditdelete='cor_complementarEditDelete', chave='codigo')
#
#     class Meta:
#         model = Cor_Complementar
#
#
class GatilForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div('nome',
                'proprietario',
                # css_class='col-md-3'
                )
        )

    class Meta:
        model = Gatil
        include_hidden = True
        fields = '__all__'


class GatilTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    nome = Column(header=u'Nome', field='nome', searchable=False)  # , header_attrs={'width': '60%'})
    proprietario = Column(header=u'Proprietario', field='proprietario')  # , header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='regraEditDelete', chave='id')

    class Meta:
        model = Gatil
        ajax = True


class RegraForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div('raca',
                'regra',
                'descricao',
                # css_class='col-md-3'
                )
        )

    class Meta:
        model = Regra
        include_hidden = True
        fields = '__all__'


class RegraTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    raca = Column(header=u'Raça', field='raca', searchable=False)  # , header_attrs={'width': '60%'})
    regra = Column(header=u'Regra', field='regra')  # , header_attrs={'width': '60%'})
    descricao = Column(header=u'Descricao', field='descricao')  # , header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='regraEditDelete', chave='id')

    class Meta:
        model = Regra
        ajax = True


class RegraInlineForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                LabelFirstDetail(""),
                Div(
                    LabelFirstDetail("Regra"),
                    InlineField('regra'),
                    css_class='col-md-4'
                ),
                Div(
                    # Hidden('uf', 'value'),
                    css_class='col-md-1'
                ),
                Div(
                    LabelFirstDetail("Descrição"),
                    InlineField('descricao'),
                    css_class='col-md-4'
                ),
                Div(
                    LabelFirstDetail(""),
                    'DELETE',
                    css_class='col-md-1'
                ),
                css_class='row',
            ),
        )

    class Meta:
        model = Regra
        fields = ['regra', 'descricao']
        can_delete = False


regraform_class = forms.inlineformset_factory(parent_model=Raca, model=Regra, form=RegraInlineForm, extra=0, min_num=0,
                                              can_delete=True)


class RacaForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                Div(
                    Div('ems', css_class='col-md-2', ),
                    Div('nome', css_class='col-md-8', ),
                    css_class='row',
                ),
                # InlineField('descricao'),
                Div(
                    Div('descricao', css_class='col-md-10', ),
                    css_class='row',
                ),
                Div(
                    Div('raca_irma', css_class='col-md-10', ),
                    css_class='row',
                ),
                Div(
                    Div('categoria', css_class='col-md-5'),
                    Div('reconhecida', css_class='col-md-5'),
                    css_class='row'),
                # css_class='row',
            )
        )

    class Meta:
        model = Raca
        include_hidden = True
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, }),
        }


class RacaTable(Table):
    ems = Column(header=u'Codigo EMS', field='ems')
    nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
    raca_irma = Column(header=u'Raça Irmã', field='raca_irma')  # , header_attrs={'width': '60%'})
    categoria = Column(header=u'Categoria', field='categoria')
    reconhecida = Column(header=u'Reconhecida', field='reconhecida')
    action = ActionColumn(vieweditdelete='racaEditDelete', chave='ems')

    class Meta:
        model = Raca


class DocumentForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                Div(
                    Div('descricao', css_class='col-md-10', ),
                    css_class='row',
                ),
                # InlineField('descricao'),
                Div(
                    Div('documento', css_class='col-md-10', ),
                    css_class='row',
                ),
                Div(
                    Div('created_by', css_class='col-md-5'),
                    Div('created_at', css_class='col-md-5'),
                    css_class='row'),
                # css_class='row',
            )
        )

    class Meta:
        model = Documento
        fields = ('descricao', 'documento', 'created_by', 'created_at')


class GatoForm(CommonModelForm):
    id = forms.IntegerField()

    def __int__(self, *args, disabled_project=True, **kwargs):
        super(GatoForm, self).__init__(*args, **kwargs)
        # self.fields['id'].disabled = True

    def layout(self):
        return Layout(
            Div('nome',
                'raca',
                'cor',
                'pai',
                'mae',
                'gatil',
                'sexo',
                'status',
                'created_by',
                'created_at',
                'modified_by',
                'modified_at',
                Field('id', readonly=False),
                # css_class='col-md-3'
                )
        )

    class Meta:
        model = Gato
        include_hidden = True
        fields = '__all__'
        widgets = {
            # 'id': forms.I(attrs={'readonly':'readonly'})
            'cor': autocomplete.ModelSelect2(url='autocomplete-regra', attrs={'style': "width: 100%", },
                                             forward=['raca']),
            'pai': autocomplete.ModelSelect2(url='autocomplete-gato-pai', attrs={'style': "width: 100%", },
                                             forward=['id'], ),
            'mae': autocomplete.ModelSelect2(url='autocomplete-gato-mae', attrs={'style': "width: 100%", },
                                             forward=['id'], ),
            #     'msg': forms.Textarea(attrs={'rows': 4, }),  # 'cols':15}),
            #     'municipio': forms.Select(choices=(('', '-- Selecione um Estado --'),)),
            #     'estado': forms.Select(choices=estado_choices,
            #                            attrs={
            #                                "onchange": "changeUF(this);",
            #                                "data-app_label": "cliente",
            #                                "data-object_name": "Municipio",
            #                            },
            #                            ),
            #     'cep': forms.TextInput(attrs={
            #         "onchange": "changeCEP(this);",
            #         "data-app_label": "cliente",
            #         "data-object_name": "Municipio",
            #     },
            #     ),
        }


class GatoTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    nome = Column(header=u'Nome', field='nome')  # , header_attrs={'width': '60%'})
    raca = Column(header=u'Raça', field='raca', searchable=False)  # , header_attrs={'width': '60%'})
    cor = Column(header=u'Cor', field='cor')  # , header_attrs={'width': '60%'})
    pai = Column(header=u'Pai', field='pai')  # , header_attrs={'width': '60%'})
    mae = Column(header=u'Mãe', field='mae')  # , header_attrs={'width': '60%'})
    gatil = Column(header=u'Gatil', field='gatil')  # , header_attrs={'width': '60%'})
    sexo = Column(header=u'Sexo', field='sexo')  # , header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='gatoEditDelete', chave='id')

    class Meta:
        model = Gato
        ajax = True
