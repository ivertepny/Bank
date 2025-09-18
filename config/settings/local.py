from os import getenv, path

from django.conf.global_settings import EMAIL_BACKEND, CSRF_TRUSTED_ORIGINS
from dotenv import load_dotenv
from .base import *
from .base import BASE_DIR


local_env_file = path.join(BASE_DIR, '.envs', '.env.local')
if path.exists(local_env_file):
    load_dotenv(local_env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')
    #'django-insecure-(%*9tjza&d(6@$o-q3#+_3n4sodzfq0c-p9@3v$c+#)y)=s^*3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG')

SITE_NAME = getenv('SITE_NAME')

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv('ADMIN_URL')

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL')
DOMAIN = getenv('DOMAIN')

MAXIMUM_UPLOAD_SIZE = 1 * 1024 * 1024  # 1 MB

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

LOCKOUT_DURATION =  timedelta(minutes=1)
LOGGING_ATTEMPTS = 3
OTP_EXPIRATION = timedelta(minutes=5)
