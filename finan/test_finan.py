# -*- coding: utf-8 -*-

from common.testcase import CRUD_Test, FTL_Test
from .models import Banco, Indice


class Finan_TestCase(FTL_Test):

    def test_banco(self):
        model = Banco
        url = 'banco'
        pk = '999'
        pk_name = 'codigoCompensacao'
        data = {pk_name: pk, 'nome': 'Xxxxx'}

        # if teste:
        #     return

        test = CRUD_Test(testcase=self, model=model, url=url, data=data, pk=pk)
        test.test_crud()

    def test_indice(self):
        model = Indice
        url = 'indice'
        pk = 'Xxxxx'
        pk_name = 'nome'
        data = {'nome': 'Xxxxx', }

        # if teste:
        #     return

        test = CRUD_Test(testcase=self, model=model, url=url, data=data, pk=pk, pk_name=pk_name, duplicidade=False)
        test.test_crud()
