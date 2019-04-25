# Register your models here.

# import django.contrib.admin
# django.contrib.admin.autodiscover()


from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from basico.models import Regra, Gato, Ninhada, Gatil


@admin.register(Gatil)
class GatilAdmin(CompareVersionAdmin):
    pass


@admin.register(Regra)
class RegraAdmin(CompareVersionAdmin):
    pass


@admin.register(Ninhada)
class NinhadaAdmin(CompareVersionAdmin):
    pass


@admin.register(Gato)
class GatoAdmin(CompareVersionAdmin):
    pass
