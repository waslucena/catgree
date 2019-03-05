# -*- coding: utf-8 -*-

from crispy_forms.bootstrap import TabHolder, Tab, Div, FieldWithButtons, StrictButton
from crispy_forms.layout import Layout, Fieldset

import common.form as common_forms
import common.layout
from table import Table
from table.columns import Column, ActionColumn
from . import models


class ConfiguracaoForm(common_forms.CommonModelForm):
    # button = Button('Button 1', 'Press Me!')
    def layout(self):
        return Layout(
            TabHolder(
                Tab(
                    'Configuração',
                    Div(
                        Div(
                            'apelido',
                            css_class='col-md-2',
                        ),
                        Div(
                            css_class='col-md-2',
                        ),
                        Div(
                            'empresa',
                            css_class='col-md-6',
                        ),
                        css_class='row'
                    ),
                    Div(
                        Div(
                            'planodecontas',
                            css_class='col-md-10',
                        ),
                        css_class='row'
                    ),
                    Div(
                        Fieldset(
                            "Contrato de Administração",
                            'contratoadm_dias',
                            'contratoadm_grupo',
                            css_class='col-md-10',
                        ),
                        css_class='row'
                    ),
                ),
                Tab(
                    'Workflows',
                    Div(
                        Div(
                            FieldWithButtons('contratoadm',
                                             StrictButton("Mostrar Workflow", name="MostrarWorkflow-contratoadm",
                                                          onclick="showWorkflow(this, 'contratoadm', 'modal-lg');")),
                            css_class='col-md-6',
                        ),
                        css_class='row'
                    ),
                    Div(
                        Div(
                            FieldWithButtons('contratoloc',
                                             StrictButton("Mostrar Workflow", name="MostrarWorkflow-contratoloc",
                                                          onclick="showWorkflow(this, 'contratoloc', 'modal-lg');")),
                            css_class='col-md-6',
                        ),
                        css_class='row'
                    ),
                    css_class='form-horizontal'
                ),
                Tab(
                    'Status',
                    Div(
                        common.layout.layout_logusuario,
                        Div(
                            Div(
                                'ativo',
                                css_class='col-md-2'
                            ),
                            css_class='row'
                        ),
                    ),
                ),
            ),
        )

    class Meta:
        model = models.Configuracao
        fields = '__all__'
        can_delete = False


class ConfiguracaoTable(Table):
    apelido = Column(header=u'Apelido', field='apelido')
    empresa = Column(header=u'Empresa', field='empresa')
    ativo = Column(header=u'Status', field='ativo')
    action = ActionColumn(vieweditdelete='configuracaoEditDelete', chave='pk')

    # @staticmethod
    # def extrajavascript(*args, **kwargs):
    #     return """ftl_workflow = riot.mount('div#workflow', 'ftl-workflow', {
    #       modal: {
    #         isvisible: true,
    #         dismissable: true,
    #         fade: true,
    #         heading: 'Workflow de Atendimento',
    #         // buttons: [{
    #         //   text: 'Ok',
    #         //   type: 'primary',
    #         //   action: function () {
    #         //     //this.close()
    #         //   }
    #         // }]
    #       },
    #       img: 'ftl-workflow-atendimento'
    #     })
    #     """

    class Meta:
        model = models.Configuracao
