# -*- coding: utf-8 -*-
from common.fields import FormSetField
from common.form import CommonModelForm, formatoNumeroZero6
from common.layout import LabelFirstDetail, layout_logusuario, glyphicon_calendar
from crispy_forms.bootstrap import InlineField, AppendedText, InlineRadios, Tab, TabHolder
from crispy_forms.layout import Layout, Div, Fieldset, Field, Row, Hidden
from dal import autocomplete
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
    action = ActionColumn(vieweditdelete='gatilEditDelete', chave='id')

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = kwargs.get('instance', None)
        self.fields['ninhada'].queryset = Ninhada.objects.filter(
            id=instance.ninhada.id if instance and instance.ninhada else None)

    def layout(self):
        return Layout(
            Row(
                Fieldset('Dados Cadastrais',
                         'nome',
                         Row(
                             Div('raca', css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div(InlineRadios('sexo'), css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div('gatil', css_class='col-sm-6'),
                             Div(InlineRadios('outcross'), css_class='col-sm-2'),
                         ),
                         Row(
                             Div('microchip', css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div(InlineRadios('lo_rx'), css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div('pedigree_anterior', css_class='col-sm-2'),
                             Div(InlineRadios('breeding'), css_class='col-sm-2'),
                             Div(InlineRadios('breeding_able'), css_class='col-sm-2'),
                             Div(
                                 AppendedText('breeding_able_date', glyphicon_calendar, data_ftl="data"),
                                 css_class='col-sm-2'),
                         ),
                         'cor',
                         Field('ninhada', disabled=True),
                         ),
            ),
            Row(
                Fieldset('Pais',
                         'pai',
                         'mae',
                         disabled='disabled',
                         ),
            ),
            Row(
                Fieldset('Status',
                         'status',
                         disabled='disabled',
                         ),
            ),
            layout_logusuario,
        )

    class Meta:
        model = Gato
        include_hidden = True
        fields = '__all__'
        fields_required = ['pai', 'mae']
        # help_texts = {
        #     # 'microchip': None,
        #     # 'pedigree_anterior': None,
        # }
        widgets = {
            # 'id': forms.I(attrs={'readonly':'readonly'})
            'gatil': autocomplete.ModelSelect2(url='autocomplete-gatil', attrs={'style': "width: 100%", }, ),
            'cor': autocomplete.ModelSelect2(url='autocomplete-regra', attrs={'style': "width: 100%", },
                                             forward=['raca', 'outcross']),
            'pai': autocomplete.ModelSelect2(url='autocomplete-gato-pai', attrs={'style': "width: 100%", },
                                             forward=['raca', 'outcross'], ),
            'mae': autocomplete.ModelSelect2(url='autocomplete-gato-mae', attrs={'style': "width: 100%", },
                                             forward=['raca', 'outcross'], ),
        }


class GatoTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    id = Column(header=u'Id', field='id', render_format=formatoNumeroZero6)  # , header_attrs={'width': '60%'})
    nome = Column(header=u'Nome', field='nome')  # , header_attrs={'width': '60%'})
    raca = Column(header=u'Raça', field='raca')  # , header_attrs={'width': '60%'})
    cor = Column(header=u'Cor', field='cor')  # , header_attrs={'width': '60%'})
    pai = Column(header=u'Pai', field='pai')  # , header_attrs={'width': '60%'})
    mae = Column(header=u'Mãe', field='mae')  # , header_attrs={'width': '60%'})
    gatil = Column(header=u'Gatil', field='gatil')  # , header_attrs={'width': '60%'})
    sexo = Column(header=u'Sexo', field='sexo')  # , header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='gatoEditDelete', chave='id')

    class Meta:
        model = Gato
        ajax = True


class GatoInlineForm(CommonModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.forms:
        self.empty_permitted = False
        self.fields['pai'].queryset = Gato.objects.none()
        self.fields['mae'].queryset = Gato.objects.none()
        self.fields['gatil'].queryset = Gato.objects.none()

    def layout(self):
        return Layout(
            Div(
                Fieldset('Filhote',
                         'nome',
                         Row(
                             Div('raca', css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div(InlineRadios('sexo'), css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div(Hidden('gatil', 'value'), css_class='col-sm-6', disabled='disabled',),
                             Div(InlineRadios('outcross'), css_class='col-sm-2'),
                             # css_class='row',
                         ),
                         Row(
                             Div('microchip', css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div(InlineRadios('lo_rx'), css_class='col-sm-2'),
                             # Div(css_class='col-xs-1'),
                             Div('pedigree_anterior', css_class='col-sm-2'),
                             Div(InlineRadios('breeding'), css_class='col-sm-2'),
                             Div(InlineRadios('breeding_able'), css_class='col-sm-2'),
                             Div(
                                 AppendedText('breeding_able_date', glyphicon_calendar, data_ftl="data"),
                                 css_class='col-sm-2'),
                             # css_class='row',
                         ),
                         'cor',
                         Field('ninhada', disabled=True),
                         ),
            ),
            Div(
                Fieldset('Pais',
                         Hidden('pai', 'value'),
                         Hidden('mae', 'value'),
                         disabled='disabled',
                         ),
                # hidden="true",
            ),
            Div(
                Fieldset('Status',
                         'status',
                         disabled='disabled',
                         ),
                hidden="true",
            ),
            Div(
                layout_logusuario,
                hidden="true",
            ),
            Div(
                'DELETE',
                css_class='col-md-1'
            ),
        )

    class Meta:
        model = Gato
        fields = '__all__'
        can_delete = False
        # exclude = ('gatil', 'pai', 'mae')
        widgets = {
            # 'id': forms.I(attrs={'readonly':'readonly'})
            # 'gatil': autocomplete.ModelSelect2(url='autocomplete-gatil', attrs={'style': "width: 100%", }, ),
            'cor': autocomplete.ModelSelect2(url='autocomplete-regra', attrs={'style': "width: 100%", },
                                             forward=['raca', 'outcross']),
            # 'pai': autocomplete.ModelSelect2(url='autocomplete-gato-pai', attrs={'style': "width: 100%", },
            #                                  forward=['raca', 'outcross'], ),
            # 'mae': autocomplete.ModelSelect2(url='autocomplete-gato-mae', attrs={'style': "width: 100%", },
            #                                  forward=['raca', 'outcross'], ),
        }


gatoform_class = forms.inlineformset_factory(parent_model=Ninhada, model=Gato, form=GatoInlineForm,
                                             extra=0, min_num=1, can_delete=True, validate_max=True, validate_min=True)

extrajavascriptNinhada = """
$(document).ready(function() {
$('#id_main-qtde').change(function(e) {
    var q = e.target.value;
    var di = $('.js-django-inlines').data('djangoInline');
    var management = $('.js-django-inlines').data('djangoInline')._getManagementForm()
    for (;parseInt(management.total_forms.value) < parseInt(q);) {
      di.addForm();
    }
    for (var i = parseInt(management.total_forms.value)-1; parseInt(management.total_forms.value) > parseInt(q); i--) {
      di.removeFormAt(i);
    }
    management.min_forms.value = q
    $("#" + management.group_id_prefix + "-MIN_NUM_FORMS").val(q);

});
function defaultSelect(main, id) {
    var ids = $('[id^=id_main-'+main+'-][id$=-'+id+']');
    ids.empty();
    ids.append('<option value="'+$('#id_main-'+id+' option:selected').val()+'" selected>'+$('#id_main-'+id+' option:selected').text()+'</option>');
};

defaultSelect('gato', 'pai');
defaultSelect('gato', 'mae');
defaultSelect('gato', 'gatil');
/*defaultSelect('gato', 'raca');*/

});

"""


class NinhadaForm(CommonModelForm):
    gato = FormSetField(formset_class=gatoform_class, show_add_button=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['gato'].empty_permitted = False
            self.fields['gato'].required.min_num = self.instance.qtde if self.instance.qtde else 1
            # self.fields['gato'].required.max_num = self.instance.qtde
            # self.fields['gato'].initial = self.instance.qtde

    @staticmethod
    def extrajavascript(*args, **kwargs):
        return extrajavascriptNinhada

    def layout(self):
        return Layout(
            TabHolder(
                Tab(
                    'Ninhada',
                    Row(
                        Row(
                            Div(AppendedText('datanasc', glyphicon_calendar, data_ftl="data"),
                                css_class='col-sm-2'),
                            Div('gatil', css_class='col-sm-6'),
                            Div(InlineRadios('outcross'), css_class='col-sm-2'),
                            Div('qtde', css_class='col-sm-2'),
                        ),
                        'pai',
                        'mae',
                    ),
                    Row(
                        Fieldset('Status',
                                 'status',
                                 disabled='disabled',
                                 # css_class='col-md-11',
                                 ),
                    ),
                    layout_logusuario,
                ),
                Tab(
                    'Filhotes',
                    InlineField('gato'),
                ),
            ),
        )

    class Meta:
        model = Ninhada
        include_hidden = True
        fields = '__all__'
        fields_required = ['pai', 'mae']
        # help_texts = {
        #     # 'microchip': None,
        #     # 'pedigree_anterior': None,
        # }
        widgets = {
            # 'id': forms.I(attrs={'readonly':'readonly'})
            'gatil': autocomplete.ModelSelect2(url='autocomplete-gatil', attrs={'style': "width: 100%", }, ),
            'pai': autocomplete.ModelSelect2(url='autocomplete-gato-pai', attrs={'style': "width: 100%", },
                                             forward=['outcross'], ),
            'mae': autocomplete.ModelSelect2(url='autocomplete-gato-mae', attrs={'style': "width: 100%", },
                                             forward=['outcross'], ),
        }


class NinhadaTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    id = Column(header=u'Id', field='id', render_format=formatoNumeroZero6)  # , header_attrs={'width': '60%'})
    gatil = Column(header=u'Gatil', field='gatil')  # , header_attrs={'width': '60%'})
    qtde = Column(header=u'Quantidade', field='qtde')  # , header_attrs={'width': '60%'})
    outcross = Column(header=u'Outcross', field='outcross')  # , header_attrs={'width': '60%'})
    pai = Column(header=u'Pai', field='pai')  # , header_attrs={'width': '60%'})
    mae = Column(header=u'Mãe', field='mae')  # , header_attrs={'width': '60%'})
    status = Column(header=u'Status', field='status')  # , header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='ninhadaEditDelete', chave='id')

    class Meta:
        model = Ninhada
        ajax = True
