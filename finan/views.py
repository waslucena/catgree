# -*- coding: utf-8 -*-


from dal import autocomplete
from django.db.models import Q

from .models import Banco


# Create your views here.


class BancoAutocomplete(autocomplete.Select2QuerySetView):
    # def get_result_value(self, result):
    #     """Return the value of a result."""
    #     if result.pk:
    #         return result.pk
    #     else:
    #         return ''

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Banco.objects.none()

        qs = Banco.objects.all()

        if self.q:
            fil = Q(nome__icontains=self.q)
            if self.q.isdigit():
                fil |= Q(codigoCompensacao=self.q)
            qs = qs.filter(fil)

        return qs.order_by('nome')
