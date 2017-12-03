"""
Django settings for incomepropertyevaluator project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import environ

'''
django-environ
https://github.com/joke2k/django-environ
'''
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env() # reading .env file

SITE_ROOT = root()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY') # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') # False if not in os.environ

ALLOWED_HOSTS = ['*']

SITE_ID = 1


# Application definition

# The following configuration forces Django to use the "ISO-8601" standard
# for the dates.
DATETIME_FORMAT = 'iso-8601'
DATETIME_INPUT_FORMATS = 'iso-8601'
DATE_FORMAT = 'iso-8601'
DATE_INPUT_FORMATS = 'iso-8601'
TIME_FORMAT = 'iso-8601'
TIME_INPUT_FORMATS = 'iso-8601'

# This configuration ensures that all authenticated users from the public
# schema to exist authenticated in the tenant schemas as well. This is
# important to have "django-tenants" work
SESSION_COOKIE_DOMAIN = '.' + env("INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN")

# The following will load up the apps.
SHARED_APPS = (
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra Django Apps
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Third Party Apps
    'django_tenants',  # (mandatory)
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    # 'django_rq', #TODO:IMPL.

     # Apps
    'shared_foundation',
    'shared_api',
    'shared_authentication',
    'shared_index'
)

TENANT_APPS = (
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',

    # Tenant-specific apps
    # ...
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',       # Third Party
    'corsheaders.middleware.CorsMiddleware',                     # Third Party
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',              # Extra Django App
    'htmlmin.middleware.HtmlMinifyMiddleware',                # Third Party
    'htmlmin.middleware.MarkRequestMiddleware',               # Third Party
    # 'shared_foundation.middleware.AcademicsTodayTokenMiddleware',
    # 'shared_foundation.middleware.AcademicsTodayIPAddressMiddleware'
]

ROOT_URLCONF = 'incomepropertyevaluator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',                   # Extra Django App
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'shared_foundation.context_processors.foundation_constants', # Custom App
            ],
        },
    },
]

WSGI_APPLICATION = 'incomepropertyevaluator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django_tenants.postgresql_backend',
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

TENANT_MODEL = "shared_foundation.SharedOrganization"

TENANT_DOMAIN_MODEL = "shared_foundation.SharedOrganizationDomain"



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
#    ('fr', ugettext('French')),
#    ('es', ugettext('Spanish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'



'''
Application Specific Variables
'''
# Variables define what URL structure to use in our system.
INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL = env("INCOMEPROPERTYEVALUATOR_APP_HTTP_PROTOCOL")
INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN = env("INCOMEPROPERTYEVALUATOR_APP_HTTP_DOMAIN")
