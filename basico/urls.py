# -*- coding: utf-8 -*-


from common import views as common_views
from django.conf.urls import url

from . import form
from . import views

urlpatterns = [
    # *common_views.include_CRUD('cor', table=form.CorTable, form=form.CorForm),
    # *common_views.include_CRUD('cor_olhos', table=form.CorOlhosTable, form=form.CorOlhosForm),
    # *common_views.include_CRUD('cor_complementar', table=form.CorComplementarTable, form=form.CorComplementarForm),
    *common_views.include_CRUD('gatil', table=form.GatilTable, form=form.GatilForm),
    *common_views.include_CRUD('raca', table=form.RacaTable, form=form.RacaForm),
    *common_views.include_CRUD('regra', table=form.RegraTable, form=form.RegraForm),
    *common_views.include_CRUD('ninhada', table=form.NinhadaTable, form=form.NinhadaForm),
    *common_views.include_CRUD('gato', table=form.GatoTable, form=form.GatoForm),

    url(r'^autocomplete-gatil/$', views.GatilAutocomplete.as_view(), name='autocomplete-gatil', ),
    url(r'^autocomplete-regra/$', views.RegraAutocomplete.as_view(), name='autocomplete-regra', ),
    url(r'^autocomplete-gato/$', views.GatoAutocomplete.as_view(), name='autocomplete-gato', ),
    url(r'^autocomplete-gato-pai/$', views.GatoAutocomplete.as_view(sexo='M'), name='autocomplete-gato-pai', ),
    url(r'^autocomplete-gato-mae/$', views.GatoAutocomplete.as_view(sexo='F'), name='autocomplete-gato-mae', ),
]
