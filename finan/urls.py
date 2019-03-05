# -*- coding: utf-8 -*-



from django.conf.urls import url

from common import form as common_forms
from common import views as common_views
from . import form
from . import views

urlpatterns = [
    *common_views.include_CRUD('banco', table=form.BancoTable, form=form.BancoForm),

    *common_views.include_CRUD('indice', table=form.IndiceTable, form=form.IndiceForm),

    url(r'^autocomplete-banco/$', views.BancoAutocomplete.as_view(), name='autocomplete-banco', ),
]
