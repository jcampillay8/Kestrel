import os
from pathlib import Path
import environ

# Inicializa el objeto Env
env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

# Lee el archivo .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = [
    ".railway.app"  # https://saas.prod.railway.app
]

if DEBUG:
    ALLOWED_HOSTS += env.list('ALLOWED_HOSTS',
                              default=['0.0.0.0', '*', 'localhost', '127.0.0.1'])


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
]

PROJECT_APPS = [
    'apps.authentication',
    'apps.skill_builder',
    'apps.skill_practice',
]

INSTALLED_APPS = BASE_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'authentication.CustomUser'

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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",
    "http://localhost:5173",
    "http://localhost:3000",

]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]


CORS_ALLOW_HEADERS = [
    'accept',
    'authorization',
    'content-type',
    'origin',
    'x-csrftoken',
    'x-requested-with',
]


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,  # Opcional, para establecer el tamaño de la página por defecto
}


CORS_ALLOW_CREDENTIALS = True

# Inicializar environ
env = environ.Env(
    # Proporcionar valores por defecto y tipo de dato para las variables
    EMAIL_PORT=(int, 587),
    EMAIL_USE_SSL=(bool, False),
    EMAIL_USE_TLS=(bool, True),
)

# Leer el archivo .env si no se ha hecho antes
environ.Env.read_env()

# ENVIRONMENT VARIABLES
WEBSITE_URL = os.environ.get('WEBSITE_URL')
EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
# GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
# GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

# SMTP SETUP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
# Conversión a int con valor por defecto 587
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'False').lower() in [
    'true', '1', 't']
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() in [
    'true', '1', 't']
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# print('EMAIL_SENDER: '+str(EMAIL_SENDER))
# print('EMAIL_BACKEND: '+str(EMAIL_BACKEND))
# print('EMAIL_HOST: '+str(EMAIL_HOST))
# print('EMAIL_PORT: '+str(EMAIL_PORT))
# print('EMAIL_USE_SSL: '+str(EMAIL_USE_SSL))
# print('EMAIL_USE_TLS: '+str(EMAIL_USE_TLS))
# print('EMAIL_HOST_USER: '+str(EMAIL_HOST_USER))
# print('EMAIL_HOST_PASSWORD: '+str(EMAIL_HOST_PASSWORD))
