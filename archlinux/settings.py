import os.path

DEPLOY_PATH = os.path.dirname(__file__) # This is the base dir for everything

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(DEPLOY_PATH, 'media')
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'archlinux.urls'

TEMPLATE_DIRS = (
    os.path.join(DEPLOY_PATH, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(DEPLOY_PATH, 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'aur',
    'registration',
    'aurprofile',
    'tagging',
    'django_openid_auth',
    'django.contrib.comments',
    'south',
)

# AUTHENTICATION_BACKENDS = (
    # 'django_openid_auth.auth.OpenIDBackend',
    # 'django.contrib.auth.backends.ModelBackend',
# )

# # Should users be created when new OpenIDs are used to log in?
# OPENID_CREATE_USERS = True

# # When logging in again, should we overwrite user details based on
# # data received via Simple Registration?
# OPENID_UPDATE_DETAILS_FROM_SREG = True

# # Tell django.contrib.auth to use the OpenID signin URLs.
# LOGIN_URL = '/openid/login'
# LOGIN_REDIRECT_URL = '/'

# Third party settings

# django-registration
ACCOUNT_ACTIVATION_DAYS = 1

# django-tagging
FORCE_LOWERCASE_TAGS = True

# Import local settings if they exist
try:
    from settings_local import *
except ImportError:
    pass
