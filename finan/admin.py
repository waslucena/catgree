# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import Banco


class BancoAdmin(admin.ModelAdmin):
    list_display = ('codigoCompensacao', 'nome')


admin.site.register(Banco, BancoAdmin)


