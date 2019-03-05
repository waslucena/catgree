# -*- coding: utf-8 -*-


from common.form import CommonModelForm
from crispy_forms.layout import Layout, Div
from table import Table
from table.columns import Column, ActionColumn

from .models import *


# class BancoForm(Bootstrap3ModelForm, forms.ModelForm):
class BancoForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div('codigoCompensacao',
                'nome',
                css_class='col-md-3'
                )
        )

    class Meta:
        model = Banco
        include_hidden = True
        fields = '__all__'


class BancoTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    codigoCompensacao = Column(header=u'Codigo Compensacao',
                               field='codigoCompensacao')  # , header_attrs={'width': '10%'})
    nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='bancoEditDelete', chave='codigoCompensacao')

    class Meta:
        model = Banco


class IndiceForm(CommonModelForm):
    def layout(self):
        return Layout(
            Div(
                'nome',
                css_class='col-md-3'
            )
        )

    class Meta:
        model = Indice
        include_hidden = True
        fields = '__all__'


class IndiceTable(Table):
    """
    Definição de ação: 1 - Add, 2 - Edit, 3 - Delete
    """
    id = Column(header=u'Código', field='id')  # , header_attrs={'width': '10%'})
    nome = Column(header=u'Nome', field='nome', header_attrs={'width': '60%'})
    action = ActionColumn(vieweditdelete='indiceEditDelete', chave='pk')

    class Meta:
        model = Indice
