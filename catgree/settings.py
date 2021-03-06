# -*- coding: utf-8 -*-

import os

import dj_database_url
from decouple import config

"""
Django settings for project.

Generated by 'django-admin startproject' using Django 1.9.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

##################################################################
# Para HEROKU / 12factor filosofy
# ALLOWED_HOSTS = ['alugarimovel.ftl.com.br', '127.0.0.1', 'demo-alugar.herokuapp.com']
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
##################################################################
# para King Host
KING = False
##################################################################

# Crispy template
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# SITE_URL = 'http://catgree.ftl.com.br:8069'
SITE_URL = 'http://www.tbridge.com.br/catgree/'

# ADMINS = ( ('was', 'was@ftl.com.br'), )
SITE_ID = 1

LOGOUT_REDIRECT_URL = SITE_URL

# O media eh onde ficarao os arquivos de upload pela administracao, fotos, videos, pdfs, etc.
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '%smedia/' % SITE_URL  # trailing slash
ADMIN_MEDIA_PREFIX = '%smedia/' % SITE_URL  # trailing slash.

# Django Compress
COMPRESS_ROOT = '/tmp/static/'
COMPRESS_ENABLED = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

#####################################################################
# Logging
# CREATE SCHEMA logging;
#
# CREATE TABLE logging.log_history (
#     id  serial,
#     tstamp timestamp DEFAULT now(),
#     schemaname text,
#     tabname text,
#     operation text,
#     who text DEFAULT current_user,
#     new_val json,
#     old_val json
# );
#
# CREATE FUNCTION change_trigger() RETURNS trigger AS $$
# BEGIN
#     IF TG_OP = 'INSERT' THEN
#         INSERT INTO logging.log_history (tabname, schemaname, operation, new_val)
#                 VALUES (TG_RELNAME, TG_TABLE_SCHEMA, TG_OP, row_to_json(NEW));
#         RETURN NEW;
#     ELSIF TG_OP = 'UPDATE' THEN
#         INSERT INTO logging.log_history (tabname, schemaname, operation, new_val, old_val)
#                 VALUES (TG_RELNAME, TG_TABLE_SCHEMA, TG_OP,
#                         row_to_json(NEW), row_to_json(OLD));
#         RETURN NEW;
#     ELSIF TG_OP = 'DELETE' THEN
#         INSERT INTO logging.log_history (tabname, schemaname, operation, old_val)
#                 VALUES (TG_RELNAME, TG_TABLE_SCHEMA, TG_OP, row_to_json(OLD));
#         RETURN OLD;
#     END IF;
# END;
# $$ LANGUAGE 'plpgsql' SECURITY DEFINER;
#
# CREATE TRIGGER trg_regra BEFORE INSERT OR UPDATE OR DELETE ON basico_regra
#         FOR EACH ROW EXECUTE PROCEDURE change_trigger();


# Application definition

INSTALLED_APPS = [
    # 'pygraphviz',
    'crispy_forms',
    'dal',
    'dal_select2',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'render_block',
    # 'debug_toolbar',
    'catgree',
    'cliente',
    'common',
    'mptt',
    'table',
    'goflow.apptools',
    'goflow.workflow',
    'goflow.runtime',
    'jasperreports',
    'finan',
    'basico',
    # 'compressor',  # django_compressor
    # 'celery',
    # 'django_celery_beat',  # a scheduler; It kicks off tasks at regular intervals, that are then executed by
    # available worker nodes in the cluster.
    # 'django_celery_results',  # This extension enables you to store Celery task results using the Django ORM
    'corsheaders',  # A Django App that adds CORS (Cross-Origin Resource Sharing) headers to responses.
    'whitenoise',
    'reversion',
    'reversion_compare',
]

# Add reversion models to admin interface:
ADD_REVERSION_ADMIN=True

# Verifica se pygraphviz está instalado, pois no HEROKU não está funcionando
try:
    from pygraphviz import AGraph
    INSTALLED_APPS.insert(0,'pygraphviz')
except:
    pass

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar
    'common.middleware.FTLMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'catgree.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            #     'admin_tools.template_loaders.Loader',
            # ],
            'debug': DEBUG,
        },
    },
]

# WSGI_APPLICATION = 'catgree.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# # Para dj-database-url: postgres://alugar:imovel@localhost:5432/alugar
#
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'alugar',
#         'USER': 'alugar',
#         'PASSWORD': 'imovel',
#         'HOST': 'localhost',
#         'OPTIONS': {
#             # 'options': '-c search_path=public,imobiliar'
#             'options': '-c search_path=public'
#         },
#
#         # 'HOST': '127.0.0.1',
#         # 'PORT': '5932',
#     },
#     # 'imobiliar': {
#     #     'ENGINE': 'django.db.backends.postgresql',
#     #     'NAME': 'imobiliar',
#     #     'USER': 'imobiliar',
#     #     'PASSWORD': 'imobiliar',
#     #     'HOST': 'localhost',
#     # },
# }

# DATABASE_ROUTERS = ['catgree.models.ImobiliarRouter']


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'pt-Br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True
USE_TZ = True

DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = '.'
DATETIME_FORMAT = 'd/m/Y H:i:s'

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

if KING:
    STATIC_URL = 'http://www.tbridge.com.br/catgree/static/'
    FORCE_SCRIPT_NAME = '/catgree'
else:
    STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')

STATICFILES_DIRS = (
    # '/home/was/alugarImovel/alugarImovel/static/',
    os.path.join(PROJECT_PATH, 'static'),
    # os.path.join(BASE_DIR, 'static'),
)

# Instead of only picking up files collected into STATIC_ROOT, find and serve files in their original directories using Django’s “finders” API
WHITENOISE_USE_FINDERS = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Controle da sessão do navegador
# Tempo de expiração da sessão
SESSION_COOKIE_AGE = 3600  # 1 hora * 60 minutos * 60 segundos
# Sessões abertas enquanto o navegador estiver aberto
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Para que a sessão seja renovada a cada requisição, basca declarar a setting:
SESSION_SAVE_EVERY_REQUEST = True

# Autenticação
if KING:
    LOGIN_URL = 'common/login/'
    LOGIN_REDIRECT_URL = '/catgree'
else:
    # LOGIN_URL = '/common/login/'
    LOGIN_URL = 'common/login/'
    LOGIN_REDIRECT_URL = '/'

# Debug toolbar
INTERNAL_IPS = {'10.0.0.99', '10.0.0.98', '192.168.0.13', '127.0.0.1'}

# Configurações Globais Alugar Imóvel
# Th
# EMPRESA_CORRENTE = 2
# PLANO_DE_CONTA_CORRENTE = 1
# TR
EMPRESA_CORRENTE = 3
PLANO_DE_CONTA_CORRENTE = 1

# Configuração dos relatórios
REPORT_SERVER_ADDR = '127.0.0.1'
REPORT_SERVER_PORT = 8080
REPORT_USERNAME = 'pedigree'
REPORT_PASSWORD = 'consulta'
REPORT_URI = 'http://%s:%s/jasperserver' % (REPORT_SERVER_ADDR, REPORT_SERVER_PORT)

# Email configuration
EMAIL_SUBJECT_PREFIX = '[Catgree] '
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'brasil.helpdesk@gmail.com'
EMAIL_HOST_PASSWORD = '@dmSerrinha!'
EMAIL_PORT = 587

# Defaul para User.email_user()
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Default para error do sistema
SERVER_EMAIL = 'wash@tbridge.com.br'

# django-cors-headers - A Django App that adds CORS (Cross-Origin Resource Sharing) headers to responses.
CORS_ORIGIN_ALLOW_ALL = True
# CORS_URLS_REGEX = r'^.*$'

# Workflow
WF_USER_AUTO = 'was'
# WF_APPS_PREFIX = '/atendimento'
WF_APPS_PREFIX = '/goflow'

# Arquivo de log
LOGGING_FILE = '/tmp/workflow.log'

# memcached / django-cache-machine
CACHES = {
    # "default": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379/1",
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #     }
    # },
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': 'unix:/tmp/memcached.sock',
        'LOCATION': '127.0.0.1:11211',
    },
}

# CELERY
CELERY_RESULT_BACKEND = 'django-db'
# For Django users the time zone specified in the TIME_ZONE setting will be used, or you can specify a custom time zone
# for Celery alone by using the timezone setting.
CELERY_TIMEZONE = TIME_ZONE
timezone = TIME_ZONE

# Test Environment
IN_TEST_MODE = False

# Diretório onde estão os relatórios do Jasper Reports
JASPERREPORTS_DIR=os.path.join(PROJECT_PATH, 'static/jasperreports/')
# Diretório onde está o JasperStarter
JASPERSTARTER_DIR = os.path.join(BASE_DIR, 'jasperreports/jasperstarter/')
# Driver de conexão do banco que deverá ter jar no diretório jdbc/ do JasperStarter
JASPERSTARTER_DRIVER={'default': '', 'skw': 'net.sourceforge.jtds.jdbc.Driver'}
# URL de conexão ao banco
JASPERSTARTER_URL={'default': '', 'skw': 'jdbc:jtds:sqlserver://10.16.0.31:1433/SANKHYA_TREINA'}
