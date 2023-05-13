from .base_settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',

    'creepyblog',

]

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
NOREPLY_EMAIL = 'noreply@creepyblog.com'
CONTACT_EMAIL = 'contact@creepyblog.com'
