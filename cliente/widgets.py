# -*- coding: utf-8 -*-



from crispy_forms.layout import Template  # Submit, Layout, Fieldset
from django.apps import apps
from django.forms.widgets import Select, Widget
from django.template import Context


class SelectMunicipioWidget(Widget):
    """
    Widget to render a <select> with the UFs (Brazillian states)
    and a <select> with the actual Municipio depending on the state
    selected
    """

    def __init__(self, *args, **kwargs):
        self.app_label = kwargs.pop('app_label', 'common')
        self.object_name = kwargs.pop('object_name', 'Municipio')
        self.mun_cls = apps.get_model(self.app_label, self.object_name)
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        attrs = attrs or {}
        if attrs:
            self.attrs.update(attrs)

        municipio_select = Select(choices=(('', '--'),))

        if value:
            try:
                municipio = self.mun_cls.objects.get(pk=value)
                uf_val = municipio.uf.pk
                mun_choices = [(m.pk, m.nome) for m in self.mun_cls.objects.filter(uf=uf_val).order_by('nome')]
                municipio_select = Select(choices=[('', '- Selecione -')] + mun_choices)
            except self.mun_cls.DoesNotExist:
                pass

        required = False
        if 'class' in self.attrs:
            required = self.attrs['class']

        select_html = municipio_select.render(name, value, self.attrs)
        template_mun = Template('<div class="field">%s</div>' % select_html)

        return template_mun.render(Context())

    class Media:
        # if HAS_REVERSE_LAZY:
        # base_url_js = reverse_lazy('common-base-url-js')
        # else:
        #    base_url_js = '/common/base_url.js'
        # js = (base_url_js, 'js/common.js',)
        # js = ('/js/common.js',)
        pass
