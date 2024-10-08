"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3b^+-4t&2t_qeo^nh@t5*s%5^ri^cs&pcq-ao@5(__)@3@i-3g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # installed apps
    'home',
    'apartments',
    'reservations',
    'contact',
    'pages',
    'blog',
    
    # third party apps
    'tinymce',
    'widget_tweaks',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static', 'static_dev'),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_prod")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from django.utils.translation import gettext_lazy as _

#Availible languages
LANGUAGES = [
    ('en', _('English')),
    # ('ru', _('Russian')),
    # ('pl', _('Polish')),
]

# tuple of dirs with files of localization
LOCALE_PATHS = (
	os.path.join(BASE_DIR, '/locale/'),
)

EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT="587"
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=True

LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = '/user/sign-in/'

TINYMCE_JS_URL = STATIC_URL + 'tinymce/js/tinymce/tinymce.min.js'
TINYMCE_JS_ROOT = STATIC_ROOT + 'tinymce/js/tinymce/'
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'modern',
    'plugins': "table,paste,searchreplace,autolink,advlist,fullpage,fullscreen,visualchars,preview,media,"
               "insertdatetime,directionality,contextmenu,wordcount",
    'theme_advanced_path_location': "bottom",
    'theme_advanced_buttons1': "fullscreen,separator,preview,separator,media,cut,copy,paste,separator,undo,redo,"
                                "separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,"
                                "underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,"
                                "justifycenter,justifyright,justifyfull,separator,help",
    'theme_advanced_buttons2': "removeformat,styleselect,formatselect,fontselect,fontsizeselect,separator,bullist,"
                                "numlist,outdent,indent,separator,link,unlink,anchor",
    'theme_advanced_buttons3': "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,"
                                "advhr,visualaid,separator,charmap,emotions,iespell,flash,separator,print",
    'mode': 'textareas',
    'theme_advanced_toolbar_location': 'top',
    'advimage_update_dimensions_onchange': True,
    'browsers': 'gecko',
    'dialog_type': 'modal',
    'object_resizing': True,
    'cleanup_on_startup': True,
    'forced_root_block': 'p',
    'remove_trailing_nbsp': True,
    'height': '400',
    'width': '1000'
}

try:
    from .settings_prod import *
except:
    pass