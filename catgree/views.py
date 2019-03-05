# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catgree.models import empresa as emp


# Create your views here.


@login_required
def index(request):
    """
    atendimentos = AtendimentoProcess.get_estatistica_status()
    atendimentosPendentes = Atendimento.get_estatistica__pendentes_prioridade()
    tarefasPendentes = Tarefas.get_estatistica_pendentes_usuario()
    conta = '5.01.01'
    saldosCaixa = SaldosMensaisPagamento.get_saldos_conta(conta)
    conta02 = '5.01.02'
    saldosCaixa02 = SaldosMensaisPagamento.get_saldos_conta(conta02)
    conta03 = '5.01.03'
    saldosCaixa03 = SaldosMensaisPagamento.get_saldos_conta(conta03)
    conta1 = '5.02.01'
    saldosCaixa1 = SaldosMensaisPagamento.get_saldos_conta(conta1)
    conta102 = '5.02.02'
    saldosCaixa102 = SaldosMensaisPagamento.get_saldos_conta(conta102)
    conta103 = '5.02.03'
    saldosCaixa103 = SaldosMensaisPagamento.get_saldos_conta(conta103)
    conta2 = '5'
    saldosCaixa2 = SaldosMensaisPagamento.get_saldos_conta(conta2)

    nb_element = 4
    xdata = range(nb_element)
    ydata = [random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)
    import decimal
    # xdata = [decimal.Decimal(10),decimal.Decimal(40),decimal.Decimal(50),decimal.Decimal(30)]
    # ydata = ['a','b','c','d']
    xdata = []
    ydata = []
    for rec in saldosCaixa:
        #xdata.append(rec.data.strftime('%m/%Y'))
        xdata.append(rec.competencia)
        ydata.append(abs(int(rec.saldoini)))

    extra_serie = {
        "tooltip": {"y_start": "There are ", "y_end": " calls"},
    }

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }

    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    """

    # Tem alteração em:
    #   pythonx.x/site-packages/nvd3/templates/content.html at line '54' and '63'
    #   pythonx.x/site-packages/nvd3/templates/piechart.html at line '18'
    # You just need to replace all the functions chart.tooltipContent to chart.tooltip.contentGenerator
    # http://stackoverflow.com/questions/35125110/django-nvd3-chart-tooltipcontent-is-not-a-function

    # xdata = []
    # ydata = []
    # for rec in saldosCaixa:
    #     xdata.append(rec.data.strftime('%m/%Y'))
    #     ydata.append(rec.saldoini)

    # extra_serie = {}
    # extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

    # chartdata = {
    #     'x': xdata,
    #     'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
    #     'name2': 'series 2', 'y2': ydata, 'extra2': extra_serie,
    # }
    # charttype = "multiBarChart"
    # data = {
    #     'charttype': charttype,
    #     'chartdata': chartdata
    # }

    # for rec in saldosCaixa:
    #     print(rec.conta,' -',rec.data.strftime('%m/%Y'), ' - ', rec.saldoini)
    # for rec in saldosCaixa:
    #     print(rec.conta,' -',rec.competencia, ' - ', rec.saldoini)

    # return render(request, 'base.html',
    #               {'empresa': emp, 'atendimentos': atendimentos, 'atendimentosPendentes': atendimentosPendentes,
    #                'tarefasPendentes': tarefasPendentes, \
    #                'conta': conta, 'saldosCaixa': saldosCaixa, 'conta02': conta02, 'saldosCaixa02': saldosCaixa02,
    #                'conta03': conta03, 'saldosCaixa03': saldosCaixa03, \
    #                'conta1': conta1, 'saldosCaixa1': saldosCaixa1, 'conta102': conta102,
    #                'saldosCaixa102': saldosCaixa102, 'conta103': conta103, 'saldosCaixa103': saldosCaixa103, \
    #                'conta2': conta2, 'saldosCaixa2': saldosCaixa2, \
    #                'chartdata': chartdata, 'charttype': charttype})
    return render(request, 'base.html', {'empresa': emp, })


def about(request):
    return render(request, 'base.html', {'empresa': emp, })


def contact(request):
    return render(request, 'contato.html', {'empresa': emp, })


@login_required
def index2(request):
    return render(request, 'base.html', {'empresa': emp, })
