"""
Django settings for bootswatch_example project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=fbvn45kes+#g1y4=&)ks$1ftfu_5tnu!ed8s4e__)nu*2*6cc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'themeswitch'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'themeswitch.context_processors.selected_theme'
)

ROOT_URLCONF = 'bootswatch_example.urls'

WSGI_APPLICATION = 'bootswatch_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


def _get_bootswatch_css_url(theme, bootstrap_version='3.1.1'):
    """
    A helper function to generate CDN URLs for bootswatch themes.
    """
    css_url = '//netdna.bootstrapcdn.com/bootswatch/%s/%s/bootstrap.min.css'
    return css_url % (bootstrap_version, theme)


BOOTSWATCHES = (
    'amelia',
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'lumen',
    'readable',
    'shamrock',
    'simplex',
    'slate',
    'spacelab',
    'superhero',
    'united',
    'yeti',
)

BOOTSWATCH_THEMES = dict(
    (theme, _get_bootswatch_css_url(theme))
    for theme in BOOTSWATCHES
)

THEMESWITCHER_THEMES = dict(
    BOOTSWATCH_THEMES,
)
