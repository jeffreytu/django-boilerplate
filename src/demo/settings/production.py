from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'www.my-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my-db-name',
        'USER': 'my-db-username',
        'PASSWORD': 'my-db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}