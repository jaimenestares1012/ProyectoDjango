
from .base import*

DEBUG = True

ALLOWED_HOSTS = []


# Application definition


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'jaime',
        'PASSWORD': 'jaimee123',
        'HOST': 'localhost',
        'PUERTO':5432, 
        
    }
}



STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')