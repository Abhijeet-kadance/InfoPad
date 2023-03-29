"""
Django settings for ideapad project.

"""

import os 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
SECRET_KEY ='django-insecure-!0^0a$zg4w$t4vog_%0_9+t&i#hg^%tbd1c-2$8p!jia4a4!d='


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = str(os.environ.get("DEBUG")) == '1'
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
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

ROOT_URLCONF = 'ideapad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'    
        ],
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

WSGI_APPLICATION = 'ideapad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME':os.environ.get("POSTGRES_DB"),
#         'USER':os.environ.get("POSTGRES_USER"),
#         'PASSWORD':os.environ.get("POSTGRES_PASSWORD"),
#         'HOST':os.environ.get("POSTGRES_HOST"),
#         'PORT':os.environ.get('POSTGRES_PORT')
#     },
# }


# DB_USERNAME=os.environ.get("POSTGRES_USER")
# DB_DATABASE=os.environ.get("POSTGRES_DB")
# DB_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
# DB_HOST=os.environ.get("POSTGRES_HOST")
# DB_PORT = os.environ.get("POSTGRES_PORT")
# DB_IS_AVAIL = all ([
#     DB_USERNAME,
#     DB_DATABASE,
#     DB_PASSWORD,
#     DB_HOST,
#     DB_PORT
# ])

# POSTGRES_READY = str(os.environ.get('POSTGRES_READY')) == "1"

# if DB_IS_AVAIL and POSTGRES_READY:
    
#     DATABASES = {
#     'default': {},
#     'users_db':{
#         'ENGINE':'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     },
#     'base_db':{
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME':os.environ.get("POSTGRES_DB"),
#         'USER':os.environ.get("POSTGRES_USER"),
#         'PASSWORD':os.environ.get("POSTGRES_PASSWORD"),
#         'HOST':os.environ.get("POSTGRES_HOST"),
#         'PORT':DB_PORT
#     },
    
# }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DATABASE_ROUTERS = ['routers.db_routers.AuthRouter']
