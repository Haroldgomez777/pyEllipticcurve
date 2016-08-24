import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dr.sqlite3',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'registration',
    'test_app',
    'myapp',
)

DEBUG = True

ALLOWED_HOSTS = ['']

SECRET_KEY = '_'

SITE_ID = 5

ROOT_URLCONF = 'test_app.urls_default'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'myapp', )
        ],
        
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Harold-Abhishek Registration Test App]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
SERVER_EMAIL = 'haroldgomez40@gmail.com'
DEFAULT_FROM_EMAIL = "Harold-Abhishek"

STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
