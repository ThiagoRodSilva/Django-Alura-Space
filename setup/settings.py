"""
Django settings for setup project.
"""
from pathlib import Path, os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-build-only')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.galeria.apps.GaleriaConfig',
    'apps.usuarios.apps.UsuariosConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'

# ====================
# BANCO DE DADOS (não mexa)
# ====================
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ====================
# CONFIGURAÇÃO T E B I (S3) - PARTES MODIFICADAS
# ====================

# Credenciais
AWS_ACCESS_KEY_ID = str(os.getenv('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = str(os.getenv('AWS_SECRET_ACCESS_KEY'))
AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))

# Configurações globais (lidas pelo django-storages e boto3)
AWS_S3_REGION_NAME = 'us-east-1'               # Região exigida pelo Tebi
AWS_S3_SIGNATURE_VERSION = 's3'                 # Assinatura versão 2 (compatível com Tebi sem erro de Content-Length)
AWS_S3_ADDRESSING_STYLE = 'path'                # Estilo de endereçamento (path)
AWS_S3_ENDPOINT_URL = 'https://s3.tebi.io'      # Endpoint do Tebi
AWS_DEFAULT_ACL = 'public-read'                  # ACL padrão
AWS_S3_FILE_OVERWRITE = False                    # Evita sobrescrever arquivos
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Backends de armazenamento
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "endpoint_url": AWS_S3_ENDPOINT_URL,
            "region_name": AWS_S3_REGION_NAME,
            "signature_version": AWS_S3_SIGNATURE_VERSION,
            "default_acl": AWS_DEFAULT_ACL,
            "location": "media",                     # Arquivos de mídia salvos em /media/
            "file_overwrite": AWS_S3_FILE_OVERWRITE,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "endpoint_url": AWS_S3_ENDPOINT_URL,
            "region_name": AWS_S3_REGION_NAME,
            "signature_version": AWS_S3_SIGNATURE_VERSION,
            "default_acl": AWS_DEFAULT_ACL,
            "location": "static",                    # Arquivos estáticos salvos em /static/
            "file_overwrite": AWS_S3_FILE_OVERWRITE,
        },
    },
}

# URLs públicas
if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/'

# Diretórios locais (necessários para collectstatic local)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'setup/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success'
}

# Configurações de Segurança para Local vs Produção
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False