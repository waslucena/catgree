# -*- coding: utf-8 -*-



from dal import autocomplete
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q, TextField
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast
from django.shortcuts import render

from .models import Pessoa, ContaBancaria


# Create your views here.

class PessoaAutocomplete(autocomplete.Select2QuerySetView):
    pessoa = "A"  # Ambos os tipos de pessoa

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Pessoa.objects.none()

        query = """SELECT pf.cpf FROM cliente_pessoafisica AS pf WHERE pf.pessoa_ptr_id = cliente_pessoa.id
                   UNION 
                   SELECT pj.cnpj FROM cliente_pessoajuridica AS pj WHERE pj.pessoa_ptr_id=cliente_pessoa.id"""

        qs = Pessoa.objects.annotate(cpfcnpj=RawSQL(query, ()))

        if self.pessoa != 'A':
            # qs = Pessoa.objects.filter(tipo=self.pessoa)
            qs = qs.filter(tipo=self.pessoa)

        if self.q:
            fil = Q(nome__icontains=self.q) | Q(cpfcnpj__icontains=self.q)
            if self.q.isdigit():
                fil |= Q(id=self.q)
            qs = qs.filter(fil)

        return qs.order_by('nome')


# @login_required
class ContaBancariaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.user.is_authenticated:
        #     return Pessoa.objects.none()

        beneficiario = self.forwarded.get('beneficiario', None)

        if not beneficiario:
            return ContaBancaria.objects.all()

        qs = ContaBancaria.objects.annotate(s_banco=Cast('banco__pk', TextField()),
                                            s_agencia=Cast('agencia', TextField()),
                                            s_conta=Cast('conta', TextField()))

        qs = qs.filter(pessoa__pk=beneficiario)

        if self.q:
            fil = Q(s_banco__icontains=self.q) | Q(s_agencia__icontains=self.q) | Q(s_conta__icontains=self.q)
            qs = qs.filter(fil)

        return qs.order_by('banco__pk', 'agencia', 'conta')


@login_required
# @permission_required('common.view_municipio', raise_exception=True)
def municipios_ajax(request, uf, app_label, object_name):
    """
    Views Ajax para pesquisa de municípios, usado na lista de formado tabela.
    """
    # /common/municipio/ajax/GO/common/Municipio/ => uf=GO app_label=cliente, object_name=Municipio
    model_cls = apps.get_model(app_label, object_name)  # apps.get_model(cliente, Municipio)
    municipio_list = model_cls.objects.filter(Q(uf=uf)).order_by('nome')
    return render(request, "%s/municipios_options.html" % app_label, {"municipio_list": municipio_list})


@login_required
# @permission_required('common.add_cep', raise_exception=True)
def cep_ajax(request, pk, app_label, object_name):
    """
    Views Ajax para pesquisa de CEPs, usado na lista de formado tabela.
    """
    # /common/cep/ajax/21020-122/common/CEP/ => uf=GO app_label=common, object_name=Municipio
    model_cls = apps.get_model(app_label, object_name)  # apps.get_model(common, Municipio)
    cep_list = model_cls.objects.filter(Q(pk=pk)).order_by('pk')
    return render(request, "%s/cep_options.html" % app_label, {"cep_list": cep_list})


@login_required
# @permission_required('common.view_municipio', raise_exception=True)
def conta_bancaria_ajax(request, pk, app_label, object_name):
    """
    Views Ajax para pesquisa de municípios, usado na lista de formado tabela.
    """
    # /cliente/contaBancaria/ajax/1/imovel/Beneficiario/ => beneficiario=1 app_label=imovel, object_name=Beneficiario
    model_cls = apps.get_model(app_label, object_name)  # apps.get_model(imovel, Beneficiario)
    conta_bancaria_list = model_cls.objects.filter(Q(pessoa_id=pk)).order_by('banco')
    return render(request, "%s/conta_bancaria_options.html" % app_label,
                  {"conta_bancaria_list": conta_bancaria_list})

