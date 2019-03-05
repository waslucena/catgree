# -*- coding: utf-8 -*-



from django.conf.urls import include, url

from common import views as common_views
from . import form
from . import views

urlpatterns = [
    *common_views.include_CRUD('estado', table=form.EstadoTable, form=form.EstadoForm),

    *common_views.include_CRUD('municipio', table=form.MunicipioTable, form=form.MunicipioForm),

    *common_views.include_CRUD('cep', table=form.CEPTable, form=form.CEPForm),

    *common_views.include_CRUD('pessoaFisica', table=form.PessoaFisicaTable, form=form.PessoaFisicaForm),

    *common_views.include_CRUD('pessoaJuridica', table=form.PessoaJuridicaTable, form=form.PessoaJuridicaForm),

    # /common/municipio/ajax/GO/cliente/Municipio/ => uf=GO app_label=cliente, object_name=Municipio
    url(r'^municipio/ajax/(?P<uf>\w+)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', views.municipios_ajax,
        name='municipios-ajax'),

    # /common/cep/ajax/21020-122/cliente/CEP/ => uf=GO app_label=cliente, object_name=Municipio
    url(r'^cep/ajax/(?P<pk>[-\w]+)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', views.cep_ajax, name='cep-ajax'),

    url(r'^contaBancaria/ajax/(?P<pk>[-\w]+)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', views.conta_bancaria_ajax,
        name='conta-bancaria-ajax'),

    url(r'^autocomplete-pessoa/$', views.PessoaAutocomplete.as_view(), name='autocomplete-pessoa', ),
    url(r'^autocomplete-pf/$', views.PessoaAutocomplete.as_view(pessoa="F"), name='autocomplete-pf', ),
    url(r'^autocomplete-pj/$', views.PessoaAutocomplete.as_view(pessoa="J"), name='autocomplete-pj', ),
    url(r'^autocomplete-contaBancaria/$', views.ContaBancariaAutocomplete.as_view(), name='autocomplete-contaBancaria', ),

    url(r'^table/', include('table.urls')),
]
