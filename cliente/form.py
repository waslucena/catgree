# -*- coding: utf-8 -*-



from crispy_forms.bootstrap import TabHolder, Tab, InlineField, Div, AppendedText
from crispy_forms.layout import Layout, Field, Fieldset
from dal import autocomplete
from django import forms

import common.form as common_forms
import common.layout
from common.fields import FormSetField
from finan.models import Banco
from table import Table
from table.columns import Column, ActionColumn
from .models import Estado, Municipio, CEP, Pessoa, PessoaFisica, PessoaJuridica, ContaBancaria

estado_choices = []# [('', '--')] + list(
    # set(Estado.objects.values_list('sigla', 'estado').distinct().order_by('sigla')))


class MunicipioForm(common_forms.CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                'ibge',
                'nome',
                'uf',
                css_class='col-md-4'
            )
        )

    class Meta:
        model = Municipio
        include_hidden = True
        fields = '__all__'
        # exclude = ['user', 'user_id', 'pessoa_ptr_id', 'tipo']


class MunicipioInlineForm(common_forms.CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                common.layout.LabelFirstDetail(""),
                Div(
                    common.layout.LabelFirstDetail("Município"),
                    InlineField('nome'),
                    css_class='col-md-4'
                ),
                Div(
                    # Hidden('uf', 'value'),
                    css_class='col-md-1'
                ),
                Div(
                    common.layout.LabelFirstDetail("Código IBGE do Município"),
                    InlineField('ibge'),
                    css_class='col-md-4'
                ),
                Div(
                    common.layout.LabelFirstDetail(""),
                    'DELETE',
                    css_class='col-md-1'
                ),
                css_class='row',
            ),
        )

    class Meta:
        model = Municipio
        fields = ['nome', 'ibge']
        can_delete = False


class MunicipioTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    ibge = Column(header=u'Código IBGE', field='ibge')
    nome = Column(header=u'Município', field='nome')  # , header_attrs={'width': '40%'})
    uf = Column(header=u'UF', field='uf', header_attrs={'width': '30%'}, searchable=False)
    action = ActionColumn(vieweditdelete='municipioEditDelete', chave='ibge')

    # search_fields = ['ibge', 'nome', 'uf__estado']
    # search_fields = ['nome']

    class Meta:
        model = Municipio
        ajax = True


municipioform_class = forms.inlineformset_factory(parent_model=Estado, model=Municipio, form=MunicipioInlineForm,
                                                   extra=0, min_num=0, can_delete=True)

class EstadoForm(common_forms.CommonModelForm):
    municipio = FormSetField(formset_class=municipioform_class)
    def layout(self):
        return Layout(
            TabHolder(
                Tab('Estado',
                    Div('sigla', 'estado', 'ibge', css_class='col-md-3'),
                ),
                Tab(
                    'Municípios',
                    Div(InlineField('municipio'), css_class='col-md-11'),
                ),
            )
        )

    class Meta:
        model = Estado
        include_hidden = True
        fields = '__all__'


class EstadoTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    sigla = Column(header=u'Sigla', field='sigla')  # , header_attrs={'width': '10%'})
    estado = Column(header=u'Estado', field='estado', header_attrs={'width': '40%'})
    ibge = Column(header=u'Código IBGE', field='ibge')  # , header_attrs={'width': '10%'})
    action = ActionColumn(vieweditdelete='estadoEditDelete', chave='sigla')

    class Meta:
        model = Estado
        std_button_pdf = True
        std_button_excel = True
        # ajax = True


class CEPForm(common_forms.CommonModelForm):
    class Meta:
        model = CEP
        include_hidden = True
        fields = '__all__'

        # estado_choices = [('', '--')] + list(
        #     set(Estado.objects.values_list('sigla', 'estado').distinct().order_by('sigla')))
        widgets = {
            'municipio': forms.Select(choices=(('', '-- Selecione um Estado --'),)),
            'estado': forms.Select(
                choices=estado_choices,
                attrs={
                    "onchange": "changeUF(this);",
                    "data-app_label": "cliente",
                    "data-object_name": "Municipio",
                },
            ),
        }

    def layout(self):
        return Layout(
            Div(
                Div(
                    Div(
                        Field('cep', data_ftl="cep"),
                        css_class='col-md-3'
                    ),
                    Div(
                        css_class='col-md-8'
                    ),
                    css_class='row'
                ),
                Div(
                    Div('endereco', css_class='col-md-11'),
                    css_class='row'
                ),
                # Div(
                #    Div('localidade', css_class='col-md-11'),
                #    css_class='row'
                # ),
                Div(
                    Div(
                        'bairro',
                        'estado',
                        css_class='col-md-5'
                    ),
                    Div(
                        # HTML(" "),
                        css_class='col-md-1'
                    ),
                    Div(
                        'municipio',
                        # HTML(" "),
                        css_class='col-md-5'
                    ),
                    css_class='row'
                ),
            ),
        )


class CEPTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    cep = Column(header=u'CEP', field='cep')
    endereco = Column(header=u'Endereco', field='endereco', header_attrs={'width': '40%'})
    bairro = Column(header=u'Bairro', field='bairro', header_attrs={'width': '20%'}, searchable=False)
    municipio = Column(header=u'Município', field='municipio', header_attrs={'width': '20%'}, searchable=False)
    action = ActionColumn(vieweditdelete='cepEditDelete', chave='cep')

    # search_fields = ['uf__estado', 'ibge', 'nome']

    class Meta:
        model = CEP
        ajax = True


class ContaBancariaInlineForm(common_forms.CommonModelForm):
    banco = forms.ModelChoiceField(
        queryset=Banco.objects.all(),
        widget=autocomplete.ModelSelect2(url='autocomplete-banco', attrs={'style': "width: 100%", }),
        # , forward=['planodecontas']) #forms.widgets.Select()
        label='Conta Bancária',
        # help_text='teste de help_text'
    )

    def layout(self):
        return Layout(
            Div(
                common.layout.LabelFirstDetail(""),
                Div(
                    common.layout.LabelFirstDetail("Banco"),
                    InlineField('banco'),
                    css_class='col-md-3'
                ),
                # Div(css_class='col-md-1'),
                Div(
                    common.layout.LabelFirstDetail("Agência"),
                    InlineField('agencia'),
                    css_class='col-md-1'
                ),
                Div(
                    common.layout.LabelFirstDetail("DV"),
                    InlineField('agencia_dv'),
                    css_class='col-md-1'
                ),
                Div(
                    common.layout.LabelFirstDetail("Conta"),
                    InlineField('conta'),
                    css_class='col-md-1'
                ),
                Div(
                    common.layout.LabelFirstDetail("DV"),
                    InlineField('conta_dv'),
                    css_class='col-md-1'
                ),
                Div(
                    common.layout.LabelFirstDetail("Tipo"),
                    InlineField('tipo_conta'),
                    css_class='col-md-2'
                ),
                Div(
                    common.layout.LabelFirstDetail("Status"),
                    InlineField('ativo'),
                    css_class='col-md-2'
                ),
                Div(
                    common.layout.LabelFirstDetail(""),
                    'DELETE',
                    css_class='col-md-1'
                ),
                css_class='row',
            ),
        )

    class Meta:
        model = ContaBancaria
        fields = '__all__'
        # fields = ['banco', 'agencia', 'agencia_dv', 'conta', 'conta_dv', 'tipo_conta', 'ativo']
        can_delete = False


contabancariaform_class = forms.inlineformset_factory(parent_model=Pessoa, model=ContaBancaria,
                                                      form=ContaBancariaInlineForm, extra=0, min_num=0, can_delete=True)


class PessoaFisicaForm(common_forms.CommonModelForm):
    contabancaria = FormSetField(formset_class=contabancariaform_class)

    def layout(self):
        return Layout(
            TabHolder(
                Tab(
                    'Informações Básicas',
                    Div(
                        Div(
                            Div('nome', css_class='col-md-11'), css_class='row'
                        ),
                        Div(
                            Div(
                                Field('cpf', data_ftl="cpf"),
                                'rg',
                                AppendedText('dataexp', common.layout.glyphicon_calendar,
                                             data_ftl="data"),
                                'estadocivil',
                                'nacionalidade',
                                'pai',
                                css_class='col-md-5'
                            ),
                            Div(
                                # HTML(" "),
                                css_class='col-md-1'
                            ),
                            Div(
                                AppendedText('datanascimento', common.layout.glyphicon_calendar, data_ftl="data"),
                                'orgaoexpedidor',
                                'passaporte',
                                'sexo',
                                'naturalidade',
                                'mae',
                                css_class='col-md-5'
                            ),
                            css_class='row'
                        ),
                    ),
                ),
                Tab(
                    'Endereço',
                    common.layout.layout_endereco,
                ),
                Tab(
                    'Contato',
                    Div(
                        Div(
                            Div(
                                'email',
                                Field('telefone', data_ftl="telefone"),
                                'usuariointernet',
                                css_class='col-md-5'
                            ),
                            Div(
                                # HTML(" "),
                                css_class='col-md-1'
                            ),
                            Div(
                                'emailnf',
                                Field('celular', data_ftl="celular"),
                                'senhainternet',
                                css_class='col-md-5'
                            ),
                            css_class='row'
                        ),
                    ),
                ),
                Tab(
                    'Status',
                    Div(
                        Fieldset('',
                                 Div(
                                     Div(
                                         'msg',
                                         css_class='col-md-11'
                                     ),
                                     css_class='row'
                                 ),
                                 Div(
                                     Div(
                                         'ativo',
                                         css_class='col-md-2'
                                     ),
                                     css_class='row'
                                 ),
                                 css_class='col-md-11'
                                 ),
                        css_class='row'
                    ),
                    common.layout.layout_logusuario,
                ),
                Tab(
                    'Contas Bancárias',
                    Div(InlineField('contabancaria'), css_class='row'),
                ),
                css_id='PF',
            ),
            # Field('slug', type='hidden'),
        )

    class Meta:
        model = PessoaFisica
        include_hidden = True
        fields = '__all__'
        exclude = ['user', 'user_id', 'pessoa_ptr_id', 'tipo']
        # estado_choices = [('', '--')] + list(
        #     set(Estado.objects.values_list('sigla', 'estado').distinct().order_by('sigla')))

        widgets = {
            'msg': forms.Textarea(attrs={'rows': 4, }),  # 'cols':15}),
            'municipio': forms.Select(choices=(('', '-- Selecione um Estado --'),)),
            'estado': forms.Select(choices=estado_choices,
                                   attrs={
                                       "onchange": "changeUF(this);",
                                       "data-app_label": "cliente",
                                       "data-object_name": "Municipio",
                                   },
                                   ),
            'cep': forms.TextInput(attrs={
                "onchange": "changeCEP(this);",
                "data-app_label": "cliente",
                "data-object_name": "Municipio",
            },
            ),
        }


class PessoaJuridicaForm(common_forms.CommonModelForm):
    contabancaria = FormSetField(formset_class=contabancariaform_class)

    def layout(self):
        return Layout(
            TabHolder(
                Tab(
                    'Informações Básicas',
                    Div(
                        Div(
                            Div('nome', css_class='col-md-11'), css_class='row'
                        ),
                        Div(
                            Div(
                                Field('cnpj', data_ftl="cnpj"),
                                'nrinscrmunicip',
                                css_class='col-md-5'
                            ),
                            Div(
                                css_class='col-md-1'
                            ),
                            Div(
                                'nrinscrestadual',
                                css_class='col-md-5'
                            ),
                            css_class='row'
                        ),
                    ),
                ),
                Tab(
                    'Endereço',
                    common.layout.layout_endereco,
                ),
                Tab(
                    'Contato',
                    Div(
                        Div(
                            Div('contato', css_class='col-md-11'), css_class='row'
                        ),
                        Div(
                            Div(
                                'email',
                                Field('telefone', data_ftl="telefone"),
                                'usuariointernet',
                                css_class='col-md-5'
                            ),
                            Div(
                                css_class='col-md-1'
                            ),
                            Div(
                                'emailnf',
                                Field('celular', data_ftl="celular"),
                                'senhainternet',
                                css_class='col-md-5'
                            ),
                            css_class='row'
                        ),
                    ),
                ),
                Tab(
                    'Status',
                    Div(
                        Fieldset('',
                                 Div(
                                     Div(
                                         'msg',
                                         css_class='col-md-11'
                                     ),
                                     css_class='row'
                                 ),
                                 Div(
                                     Div(
                                         'ativo',
                                         css_class='col-md-2'
                                     ),
                                     css_class='row'
                                 ),
                                 css_class='col-md-11'
                                 ),
                        css_class='row'
                    ),
                    common.layout.layout_logusuario,
                ),
                Tab(
                    'Contas Bancárias',
                    Div(InlineField('contabancaria'), css_class='row'),
                ),
                css_id='PJ',
            ),
            # Field('slug', type='hidden'),
        )

    class Meta:
        model = PessoaJuridica
        include_hidden = True
        fields = '__all__'
        exclude = ['user', 'user_id', 'tipo']  # , 'pessoa_ptr_id'
        # estado_choices = [('', '--')] + list(
        #     set(Estado.objects.values_list('sigla', 'estado').distinct().order_by('sigla')))

        widgets = {
            'msg': forms.Textarea(attrs={'rows': 4, }),  # 'cols':15}),
            'municipio': forms.Select(choices=(('', '-- Selecione um Estado --'),)),
            'estado': forms.Select(choices=estado_choices,
                                   attrs={
                                       "onchange": "changeUF(this);",
                                       "data-app_label": "cliente",
                                       "data-object_name": "Municipio",
                                   },
                                   ),
            'cep': forms.TextInput(attrs={
                "onchange": "changeCEP(this);",
                "data-app_label": "cliente",
                "data-object_name": "Municipio",
            },
            ),
        }


class PessoaTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """

    id = Column(header=u'Id', field='id', render_format=common_forms.formatoNumeroZero6)
    nome = Column(header=u'Nome', field='nome')  # , header_attrs={'class': 'alert-info'})
    tipo = Column(header=u'Tipo', field='tipo')
    telefone = Column(header=u'Fixo', field='telefone')
    celular = Column(header=u'Celular', field='celular')
    ativo = Column(header=u'Status', field='ativo')  # , attrs={'title': A('ativo')})

    class Meta:
        model = Pessoa
        ajax = True


class PessoaFisicaTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """

    id = Column(header=u'Id', field='id', render_format=common_forms.formatoNumeroZero6)
    nome = Column(header=u'Nome', field='nome')
    cpf = Column(header=u'CPF', field='cpf')
    telefone = Column(header=u'Fixo', field='telefone')
    celular = Column(header=u'Celular', field='celular')
    ativo = Column(header=u'Status', field='ativo')
    action = ActionColumn(vieweditdelete='pessoaFisicaEditDelete', chave='id')

    class Meta:
        model = PessoaFisica
        ajax = True


class PessoaJuridicaTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    id = Column(header=u'Id', field='id', render_format=common_forms.formatoNumeroZero6)
    nome = Column(header=u'Nome', field='nome')
    cnpj = Column(header=u'CNPJ', field='cnpj')
    telefone = Column(header=u'Fixo', field='telefone')
    celular = Column(header=u'Celular', field='celular')
    ativo = Column(header=u'Status', field='ativo')
    action = ActionColumn(vieweditdelete='pessoaJuridicaEditDelete', chave='id')

    class Meta:
        model = PessoaJuridica
        ajax = True


