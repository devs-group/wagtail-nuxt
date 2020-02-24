from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ENABLE_DEBUG_BAR = False
WAGTAIL_CACHE = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


if ENABLE_DEBUG_BAR is True and DEBUG is True:

    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar',
    ]

    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1", "172.28.0.1")

try:
    from .local import *
except ImportError:
    pass
