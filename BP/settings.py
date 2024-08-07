"""
Django settings for BP project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Find templates in the same folder as settings.py.
SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SETTINGS_PATH, 'ican/templates/indexauth'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^tf_$@%v#kaf8eev@6u^+c2o^$p3=lew1g4s9b9x9$607-(7vs'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'ican',
    'django_social_share',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
]

ROOT_URLCONF = 'BP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['ican/templates/indexauth'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'BP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'businessdb',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'root',
        'PORT': '3307',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL='/images/'
MEDIA_ROOT=BASE_DIR/'static'

STATICFILES_DIRS=[
    BASE_DIR/'static'
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# social appcustom settings

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'login_page'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_URL = 'logout_page'
LOGOUT_REDIRECT_URL = 'login_page'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  '440859543942-7tk84n5uu6ra0ks0k3708dk0f32ema9h.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET =  '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'





# IT IS MAIL CODES FROM DJANGO

EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT = '587'
# EMAIL_HOST_USER = 'captcha486@gmail.com'
# EMAIL_HOST_PASSWORD = 'uslppmdmgcufzteg'
EMAIL_HOST_USER = 'teramediainfo@gmail.com'
EMAIL_HOST_PASSWORD = 'mnsspdxsdqlrxcdl'
EMAIL_USE_TLS =True
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

