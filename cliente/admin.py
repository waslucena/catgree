# -*- coding: utf-8 -*-



from django.contrib import admin

from .models import PessoaFisica, PessoaJuridica, Estado, Municipio, CEP

"""
# Register your models here.


class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'endereco', 'cep', 'email')
    #list_display = ('nome', 'endereco')
    #list_filter = ['tipo', 'estado']
    list_filter = ['bairro', 'estado']
    #prepopulated_fields = {'slug': ('nome',)}
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class PessoaFisicaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'endereco', 'cep', 'email')
    #list_display = ('nome', 'endereco')
    list_filter = ['bairro', 'estado']
    #prepopulated_fields = {'slug': ('cpf',)}
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class PessoaJuridicaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'endereco', 'cep', 'email')
    #list_display = ('nome', 'endereco')
    list_filter = ['bairro', 'estado']
    #prepopulated_fields = {'slug': ('cnpj',)}
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

#admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)

"""


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'estado', 'ibge')


admin.site.register(Estado, EstadoAdmin)


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('ibge', 'nome', 'uf')
    raw_id_fields = ('uf',)


admin.site.register(Municipio, MunicipioAdmin)


class CEPAdmin(admin.ModelAdmin):
    list_display = ('cep', 'endereco', 'bairro', 'municipio', 'estado')
    raw_id_fields = ('municipio', 'estado')


admin.site.register(CEP, CEPAdmin)


class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'email',
        'emailnf',
        'msg',
        'telefone',
        'celular',
        'ativo',
        'usuariointernet',
        'senhainternet',
        'endereco',
        'enderecoNumero',
        'complemento',
        'bairro',
        'municipio',
        'estado',
        'cep',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
        'tipo',
        # 'slug',
    )
    list_filter = (
        'ativo',
        'bairro',
        'estado',
    )
    # search_fields = ('slug',)
    date_hierarchy = 'created_at'


class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'email',
        'emailnf',
        'msg',
        'telefone',
        'celular',
        'ativo',
        'usuariointernet',
        'senhainternet',
        'endereco',
        'enderecoNumero',
        'complemento',
        'bairro',
        'municipio',
        'estado',
        'cep',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
        'tipo',
        # 'slug',
        'cpf',
        'rg',
        'orgaoexpedidor',
        'dataexp',
        'sexo',
        'datanascimento',
        'estadocivil',
        'nacionalidade',
        'naturalidade',
        'pai',
        'mae',
        'passaporte',
    )
    list_filter = (
        'ativo',
        'bairro',
        'estado',
    )
    # search_fields = ('slug',)
    date_hierarchy = 'created_at'


admin.site.register(PessoaFisica, PessoaFisicaAdmin)


class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'email',
        'emailnf',
        'msg',
        'telefone',
        'celular',
        'ativo',
        'usuariointernet',
        'senhainternet',
        'endereco',
        'enderecoNumero',
        'complemento',
        'bairro',
        'municipio',
        'estado',
        'cep',
        'created_by',
        'created_at',
        'modified_by',
        'modified_at',
        'tipo',
        # 'slug',
        'cnpj',
        'contato',
        'nrinscrmunicip',
        'nrinscrestadual',
    )
    list_filter = (
        'ativo',
        'bairro',
        'estado',
    )
    # search_fields = ('slug',)
    date_hierarchy = 'created_at'


admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
