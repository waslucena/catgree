# -*- coding: utf-8 -*-

# from selenium.webdriver.support import expected_conditions as EC
#
# from common.testcase import FTL_Html_Test
#
#
# class Test(FTL_Html_Test):
#     def test_estado(self):
#         # Insert
#         self.wait(url='#/cliente/estado/add/')
#         self.set_element_by_id('id_main-sigla', 'XX')
#         self.set_element_by_id('id_main-estado', 'Xxxxx')
#         self.set_element_by_id('id_main-ibge', 'xx')
#         self.click_element_by_id(id='submit-id-save')
#         # Teste de erro no Save
#         self.assertFalse(self.is_element_present_by_id('div_id_main-sigla'), 'Save do Insert')
#
#         # Teste de duplicidade
#         self.wait(url='#/cliente/estado/add/')
#         self.set_element_by_id('id_main-sigla', 'XX')
#         self.set_element_by_id('id_main-estado', 'Xxxxx')
#         self.set_element_by_id('id_main-ibge', 'xx')
#         self.click_element_by_id(id='submit-id-save')
#         self.check_has_error_by_id('div_id_main-sigla', 'Não identificou duplicidade de Estado')
#
#         # Update
#         self.wait(url='#/cliente/estado/XX/2/')
#         self.click_element_by_link_text('Município')
#         self.click_element_by_css_selector('a.js-django-inlines-add-form-nested-cliente-estado')
#         self.set_element_by_id('id_nested-cliente-estado-0-nome', 'xxxx')
#         self.set_element_by_id('id_nested-cliente-estado-0-ibge', '1111111')
#         self.click_element_by_xpath('// form / ul[@ class ="nav nav-tabs"] / li[@ class ="tab-pane"] / a')
#         self.click_element_by_id(id='submit-id-save')
#         # Teste de erro Save
#         self.assertFalse(self.is_element_present_by_id('div_id_main-sigla'), 'Save do Update')
#
#         # Delete de Município
#         self.wait(url='#/cliente/estado/XX/2/')
#         self.click_element_by_link_text('Município')
#         self.set_checkbox_by_id('id_nested-cliente-estado-0-DELETE')
#         self.click_element_by_xpath('// form / ul[@ class ="nav nav-tabs"] / li[@ class ="tab-pane"] / a')
#         self.click_element_by_id(id='submit-id-save')
#         # Teste de erro Save
#         self.assertFalse(self.is_element_present_by_id('div_id_main-sigla'), 'Save do Delete de Município')
#
#         # Delete de Estado
#         self.wait(url='#/cliente/estado/XX/3/')
#         self.click_element_by_id(id='submit-id-delete')
#         self.assertFalse(self.is_element_present_by_name('cancel'), 'Save do Delete de Estado')
#
#     def test_pf(self):
#         self.click_element_by_link_text("Cadastros")
#         self.click_element_by_link_text("Clientes")
#         self.click_element_by_link_text(u"Pessoa Física")
#         self.wait(url='#/cliente/pessoaFisica/add/')
#         self.set_element_by_id('id_main-nome', 'Xambios')
#         self.set_element_by_id('id_main-cpf', '211.111.111-20')
#         self.set_element_by_id('id_main-rg', '111111111')
#         self.set_datepicker_by_id('id_main-dataexp', '09/09/1990')
#         self.set_datepicker_by_id('id_main-datanascimento', '15/09/1970')
#         self.set_element_by_id('id_main-nacionalidade', 'Brasileira')
#         self.set_element_by_id('id_main-pai', 'Zé')
#         self.set_element_by_id('id_main-mae', 'Maria')
#         self.set_select_by_id("id_main-estadocivil", "Solteiro")
#         self.set_select_by_id("id_main-sexo", "Masculino")
#         self.set_element_by_id('id_main-orgaoexpedidor', 'IFP/RJ')
#
#         self.click_element_by_link_text('Endereço')
#         self.set_element_by_id('id_main-cep', '21020-122')
#         self.set_element_by_id('id_main-endereco', 'Avenida Lobo Júnior')
#         self.set_element_by_id('id_main-enderecoNumero', '1604')
#         self.set_element_by_id('id_main-bairro', 'Penha Circular')
#         self.set_select_by_id('id_main-estado', 'Rio de Janeiro')
#         self.wait_for_loaded()
#         self.set_select_by_id('id_main-municipio', 'Rio de Janeiro')
#
#         self.click_element_by_link_text('Contato')
#         self.set_element_by_id('id_main-email', 'ze@qualquer.com.br')
#         self.set_element_by_id('id_main-emailnf', 'ze@qualquer.com.br')
#         self.click_element_by_link_text("Informações Básicas")
#         self.click_element_by_id('submit-id-save')
#
#         self.set_element_by_css_selector("input.form-control.input-sm", "Xambios")
#         self.wait_by_css_selector(css='i.fa.fa-pencil', msg='Não achou botão de edição')
#         self.click_element_by_css_selector("i.fa.fa-pencil")
#         self.check_value_by_id("id_main-nome", "Xambios", 'Não encontrou registro salvo com nome Xambios')
#         self.set_element_by_id("id_main-nome", "Xambios Mané")
#         self.click_element_by_id("submit-id-save")
#
#         self.wait_for_loaded()
#         self.click_element_by_css_selector("i.fa.fa-pencil")
#         self.wait_for_loaded()
#         self.click_element_by_link_text(u"Conta Bancária")
#         self.click_element_by_link_text(u"Adicionar Conta Bancária")
#
#         #self.click_element_by_xpath('//span[@aria-label="select2-id_nested-cliente-pessoafisica-0-banco-container"]')
#
#         self.set_element_by_id('id_nested-cliente-pessoafisica-0-banco', '341')
#         self.set_element_by_id('id_nested-cliente-pessoafisica-0-agencia', '1234')
#         self.set_element_by_id('id_nested-cliente-pessoafisica-0-agencia_dv', '5')
#         self.set_element_by_id('id_nested-cliente-pessoafisica-0-conta', '12345')
#         self.set_element_by_id('id_nested-cliente-pessoafisica-0-conta_dv', '6')
#         self.click_element_by_link_text("Pessoa Física")
#         self.click_element_by_id("submit-id-save")
#
#         self.click_element_by_css_selector("i.fa.fa-pencil")
#         self.click_element_by_link_text(u"Conta Bancária")
#         self.click_element_by_id('id_nested-cliente-pessoafisica-0-DELETE')
#         self.click_element_by_link_text("Pessoa Física")
#         self.click_element_by_id("submit-id-save")
#
#         self.click_element_by_css_selector("i.fa.fa-trash-o")
#         self.click_element_by_id("submit-id-delete")
#         self.click_element_by_css_selector("i.fa.fa-close")
#
# # if __name__ == "__main__":
# #     unittest.main()
import datetime

from django.utils import timezone

from common.testcase import CRUD_Test, FTL_Test
from .models import Estado, Municipio, CEP, PessoaFisica, PessoaJuridica, ContaBancaria


class Cliente_TestCase(FTL_Test):

    def post_update_estado(self, pk, model, formset_delete):
        q = model.objects.get(pk=pk).municipio_set.all()
        if formset_delete:
            msg = 'Não deletou município'
        else:
            msg = 'Não tem município'
        self.assertTrue(q.exists() ^ formset_delete, msg=msg)

    def test_estado(self):
        # Total de estados deve ser 28 = 26 + DF + EX
        self.assertEqual(28, len(Estado.objects.all()))

        model = Estado
        url = 'estado'
        pk = 'XX'
        pk_name = 'sigla'
        data = {pk_name: pk, 'estado': 'Xxxxx', 'ibge': 'xx'}

        formset = [{'prefix': 'nested-cliente-estado',
                    'data': [{'nome': 'xxxx', 'ibge': '909090'}],
                    'formset_pk_name': 'uf',
                    'model': Municipio,
                    'fk': None,
                    'fk_name': None,
                    'widget': False,
                    'insert': False,
                    'update': True,
                    'delete': True}]

        test = CRUD_Test(testcase=self, model=model, url=url, pk=pk, pk_name=pk_name, data=data,
                         formset=formset,)

        # Faz todos os testes sem o insert de município
        test.test_crud()

        # Inclusão
        test.test_insert()

        # Update
        # Testa se criou município
        self.qtde = 1
        test.test_update(post_update=self.post_update_estado)

        # Update
        # Testa se deletou município
        self.qtde = 0
        test.test_update(post_update=self.post_update_estado, formset_delete=True)

        # formset_delete
        test.test_delete()

    def test_municipio(self):
        model = Municipio
        url = 'municipio'
        pk = '111111'
        pk_name = 'ibge'
        data = {pk_name: pk, 'nome': 'Xxxxx', 'uf': 'EX'}

        # if teste:
        #     return

        test = CRUD_Test(testcase=self, model=model, url=url, data=data, pk=pk)
        test.test_crud()

    def test_cep(self):
        model = CEP
        url = 'cep'
        pk = '99999-999'
        pk_name = 'cep'
        data = {pk_name: pk, 'endereco': 'Rua do Sobe e Desce 30', 'bairro': 'Qualquer Lugar',
                'municipio': '1200013', 'estado': 'AC'}

        # if teste:
        #     return

        test = CRUD_Test(testcase=self, model=model, url=url, data=data, pk=pk, pk_name=pk_name)
        test.test_crud()

    def test_pf(self):
        m = Municipio.objects.get(nome='Rio de Janeiro')

        # login()

        model = PessoaFisica
        url = 'pessoaFisica'
        pk = '211.111.111-20'
        pk_name = 'cpf'
        data = {'nome': 'Xambios',
                pk_name: pk,
                'rg': '111111111',
                'dataexp': datetime.datetime.strptime('09/09/1990', '%d/%m/%Y').date(),
                'datanascimento': datetime.datetime.strptime('15/09/1990', '%d/%m/%Y').date(),
                'nacionalidade': 'Brasileira',
                'pai': 'Zé',
                'mae': 'Maria',
                'estadocivil': 'S',
                'sexo': 'M',
                'orgaoexpedidor': 'IFP/RJ',

                # Endereço
                'cep': '21020-122',
                'endereco': 'Avenida Lobo Júnior',
                'enderecoNumero': '1604',
                'bairro': 'Penha Circular',
                'estado': 'RJ',

                'municipio': m.pk,

                # Contato
                'email': 'ze@qualquer.com.br',
                'emailnf': 'ze@qualquer.com.br',
                'created_at': timezone.now().strftime('%d/%m/%Y'),
                'modified_at': timezone.now().strftime('%d/%m/%Y 00:00:00'),
                'slug': '1',
                }

        formset = [{'prefix': 'nested-cliente-pessoafisica',
                    'data': [{'banco': '341', 'agencia': '1234', 'agencia_dv': 'XX', 'conta': '654321', 'conta_dv': '2',
                         'tipo_conta': '1', 'ativo': 'S'}, ],
                    'formset_pk_name': 'pessoa',
                    'model': ContaBancaria,
                    'fk': None,
                    'fk_name': 'id',
                    'widget': False,
                    'insert': False,
                    'update': False,
                    'delete': True}]

        test = CRUD_Test(testcase=self, model=model, url=url, pk=pk, pk_name=pk_name, data=data,
                         formset=formset, duplicidade=False)
        test.test_crud()

    def test_pj(self):
        m = Municipio.objects.get(nome='Rio de Janeiro')

        # login()

        model = PessoaJuridica
        url = 'pessoaJuridica'
        pk = '73.055.097/0001-03'
        pk_name = 'cnpj'
        data = {'nome': 'Xambios',
                pk_name: pk,
                'nacionalidade': 'Brasileira',
                'nrinscrmunicip': 'insc munic',
                'nrinscrestadual': 'insc estad',
                'contato': 'Zé Qualquer',

                # Endereço
                'cep': '21020-122',
                'endereco': 'Avenida Lobo Júnior',
                'enderecoNumero': '1604',
                'bairro': 'Penha Circular',
                'estado': 'RJ',

                'municipio': m.pk,

                # Contato
                'email': 'ze@qualquer.com.br',
                'emailnf': 'ze@qualquer.com.br',
                'created_at': timezone.now().strftime('%d/%m/%Y'),
                'modified_at': timezone.now().strftime('%d/%m/%Y 00:00:00'),
                'slug': '1',
                }

        formset = [{'prefix': 'nested-cliente-pessoajuridica',
                    'data': [{'banco': '341', 'agencia': '1234', 'agencia_dv': 'XX', 'conta': '654321', 'conta_dv': '2',
                         'tipo_conta': '1', 'ativo': 'S'}, ],
                    'formset_pk_name': 'pessoa',
                    'model': ContaBancaria,
                    'fk': None,
                    'fk_name': 'id',
                    'widget': False,
                    'insert': False,
                    'update': False,
                    'delete': True}]

        test = CRUD_Test(testcase=self, model=model, url=url, pk=pk, pk_name=pk_name, data=data,
                         formset=formset, duplicidade=False)
        test.test_crud()
