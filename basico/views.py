from dal import autocomplete
from django.db.models import TextField, Q
from django.db.models.functions import Cast
from django.shortcuts import render

# Create your views here.

# @login_required
from basico.models import Regra, Gato


class RegraAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Regra.objects.none()

        raca = self.forwarded.get('raca', None)

        if not raca:
            return Regra.objects.all()

        qs = Regra.objects.annotate(s_regra=Cast('regra', TextField()), s_descricao=Cast('descricao', TextField()))

        qs = qs.filter(raca__pk=raca)

        if self.q:
            fil = Q(s_regra__icontains=self.q) | Q(s_descricao__icontains=self.q)
            qs = qs.filter(fil)

        return qs.order_by('regra', 'descricao')


class GatoAutocomplete(autocomplete.Select2QuerySetView):
    sexo = "A"  # Ambos os sexos

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Pessoa.objects.none()

        qs = Gato.objects.all()

        if self.sexo != 'A':
            # qs = Pessoa.objects.filter(tipo=self.pessoa)
            qs = qs.filter(sexo=self.sexo)

        id = self.forwarded.get('id', None)

        if id:
            qs = qs.exclude(id=id)

        if self.q:
            fil = Q(nome__icontains=self.q) | Q(gatil__icontains=self.q) | \
                  Q(raca__icontains=self.q) | Q(cor__icontains=self.q)
            if self.q.isdigit():
                fil |= Q(id=self.q)
            qs = qs.filter(fil)

        return qs.order_by('nome', 'gatil', 'raca', 'cor')


