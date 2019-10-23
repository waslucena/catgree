from dal import autocomplete
from django.db.models import TextField, Q
from django.db.models.functions import Cast

# @login_required
from basico.models import Regra, Gato, Raca, Gatil


# Create your views here.


class GatilAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Gatil.objects.none()

        qs = Gatil.objects.all()

        if self.q:
            fil = Q(nome__icontains=self.q) | Q(proprietario__nome__icontains=self.q)
            qs = qs.filter(fil)

        return qs.order_by('nome', 'proprietario')


class RegraAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Regra.objects.none()

        raca = self.forwarded.get('raca', None)

        if not raca:
            # return Regra.objects.all()
            return Regra.objects.none()

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

        # Se não está autenticado ou se não tem raca, então retorna
        if not self.request.user.is_authenticated:
            return Regra.objects.none()

        ems = self.forwarded.get('raca', None)

        # Só podem ser pai/mãe os gatos que são da mesma raça ou de raças irmãs
        # Se outcross então não faz filtragem por raça
        outcross = self.forwarded.get('outcross', None)
        if outcross and outcross == 'N' and ems:
            raca = Raca.objects.get(ems=ems)
            racas = (raca.ems + ((',' + raca.raca_irma) if raca.raca_irma else '')).replace(' ', '')
            qs = Gato.objects.filter(raca__ems__in=racas.split(','))
        else:
            qs = Gato.objects.all()

        if self.sexo != 'A':
            # qs = Pessoa.objects.filter(tipo=self.pessoa)
            qs = qs.filter(sexo=self.sexo)
        id = self.forwarded.get('id', None)

        if id:
            qs = qs.exclude(id=id)

        if self.q:
            # qq = self.q.split(' ')
            fil = Q()
            for s in self.q.split(' '):
                fil = fil & \
                      (Q(nome__icontains=s) | Q(gatil__nome__icontains=s) |
                       Q(raca__nome__icontains=s) | Q(cor__regra__icontains=s) |
                       Q(pedigree_anterior__icontains=s))
                if s.isdigit():
                    fil |= Q(id=s)
            # if self.q.isdigit():
            #     fil |= Q(id=self.q)
            qs = qs.filter(fil)

        return qs.order_by('nome', 'gatil', 'raca', 'cor')
