# -*- coding: utf-8 -*-

from django.apps import AppConfig


class CatgreeConfig(AppConfig):
    name = 'catgree'
    verbose_name = 'Cat Pedigree'
    label = 'catgree'

    def ready(self):
        pass  # startup code here
