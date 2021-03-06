# -*- coding: utf-8 -*-
# Django settings for golfdoksy project.
import os
import sys
import logging
gettext = lambda s: s


if 'prod' in os.uname()[1]:
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

GENERAL_SUPPORT_EMAIL = 'robert.smol@stereoit.com'
ADMINS = (
     ('Robert Smol', GENERAL_SUPPORT_EMAIL),
)

PROJECT_ROOT = '%s' % os.path.dirname(os.path.abspath(__file__))
rel_path = lambda p: os.path.join(PROJECT_ROOT,p)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel_path('db.sql'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'
#LANGUAGE_CODE = 'en'

#django CMS
LANGUAGES = [
    ('en', 'English'),
    ('cs', 'Czech'),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = rel_path('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = rel_path('/static/')
if DEBUG:
    STATIC_ROOT = rel_path('final_static')
else:
    STATIC_ROOT = '/srv/staticfiles/golfdoksy.cz/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel_path('static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7jnz$1v1n4qpok54c40i&0y^4o5uje+4ps@2^xd2=h^&n3&d6%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'tournaments.context_processors.have_tournaments',
    'social_auth.context_processors.social_auth_by_type_backends',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel_path('templates'),
)

FILER_IMAGE_USE_ICON = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    #'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.text',
    'cms.plugins.twitter',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'sorl.thumbnail',
    'django.contrib.admin',
    'contact',
    'news',
    'photologue',
    'partners',
    'players',
    'tournaments',
#    'django_openid_auth',
    'social_auth',
)

CMS_TEMPLATES = (
    ('homepage.html', 'Homepage'),
    ('clean.html', 'Clean page'),
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

LOG_BASE_PATH = os.path.join(os.path.split(PROJECT_ROOT)[0], 'logs')

#LOGIN_URL = '/hraci/login/'
#LOGIN_REDIRECT_URL = '/'
#LOGIN_URL = '/openid/login/'
#LOGIN_REDIRECT_URL = '/admin/'
#OPENID_CREATE_USERS = True
#OPENID_UPDATE_DETAILS_FROM_SREG = False
#OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/site-xrds?hd=golfdoksy.cz'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
#    'django_openid_auth.auth.OpenIDBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    #'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.OpenIDBackend',
)

AUTH_PROFILE_MODULE = 'players.PlayerProfile'

#OAuth keys
TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'


SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/account-created/'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_DEFAULT_USERNAME = 'golfdoksy_user'
SOCIAL_AUTH_UUID_LENGTH = 16

SOCIAL_AUTH_EXPIRATION = 'expires'

SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

GOOGLE_DISPLAY_NAME     = 'Golf Club Doksy'
GOOGLE_CONSUMER_KEY     = 'www.golfdoksy.cz '
GOOGLE_CONSUMER_SECRET  = 'yAwme-rbIWFHZ3SVKKKD305k'

GOOGLE_OAUTH2_CLIENT_ID = '842489790353.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'A5jQM__6kzg8Mc2dUQBYxjWq'

TWITTER_CONSUMER_KEY    = 'm1h5iw0z5P7iIqHLxBa3cA'
TWITTER_CONSUMER_SECRET = '77Hbl5xiTUPuamiPiFZZfxsxWmVKpbD34jqxGGaQAHo'

#tests
TEST_GOOGLE_USER = 'robert.smol@golfdoksy.cz'
TEST_GOOGLE_PASSWORD = 'ef0iwenf13jasdfb'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_all': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_BASE_PATH, 'all.log'),
            'mode': 'a'
        },
        'file_sql': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_BASE_PATH, 'sql.log'),
            'mode': 'a'
        },

    },
    'loggers': {
        '': {
            'handlers': ['file_all',],
            'level': 'DEBUG'
        },
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.db.backends': {
            'propagate': False,
            'handlers': ['file_sql'],
            'level': 'DEBUG'
        },
    }
}
