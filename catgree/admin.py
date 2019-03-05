# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Configuracao

admin.site.site_header = u"Administração do Site"
admin.site.index_title = u"Administração do Site"
admin.site.site_title = u"Site de Administração do Catgree"


class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'apelido',
        'empresa',
        # 'planodecontas',
        'ativo',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
    )
    list_filter = (
        'empresa',
        # 'planodecontas',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
    )
    date_hierarchy = 'created_at'


admin.site.register(Configuracao, ConfiguracaoAdmin)
