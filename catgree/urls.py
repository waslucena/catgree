# - * - coding: utf-8 - * -

""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from common import views as common_views
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.static import serve

from . import form
from . import views

# monta modal do help do workflow
# extrajavascriptWorkflow = """ftl_workflow = riot.mount('div#workflow', 'ftl-workflow', {
#   modal: {
#     isvisible: true,
#     dismissable: true,
#     fade: true,
#     heading: 'Workflow de Atendimento',
#     // buttons: [{
#     //   text: 'Ok',
#     //   type: 'primary',
#     //   action: function () {
#     //     //this.close()
#     //   }
#     // }]
#   },
#   img: 'ftl-workflow-atendimento'
# })
# """

admin.autodiscover()

# from imovel.form import FiancaFormSet
# from imovel.models import Fianca
# def x(request):
#     q = Fianca.objects.filter(id=2)
#     form = FiancaFormSet(queryset=q)  # , instance=mymodel)
#     form.show_add_button = False
#     return render_to_response('p.html', {'formset': form})


urlpatterns = [
    # Configurações globais
    url(r'^about', views.about, name="about"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    *common_views.include_CRUD('configuracao', table=form.ConfiguracaoTable, form=form.ConfiguracaoForm),

    # url(r'^atendimento/', include('atendimento.urls')),
    url(r'^basico/', include('basico.urls')),
    url(r'^cliente/', include('cliente.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^finan/', include('finan.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/Keys.ico', permanent=True)),
    # url(r'^teste', views.index2, name='index2'),
    # url(r'^x', x, name='index3'),
    url(r'^$', views.index, name='index'),
    url(r'^goflow/', include('goflow.urls', namespace='goflow')),

    # url(r'^ajax_select/', include(ajax_select_urls)),
]
