from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xuxeq#ri03)088)_inw-8kt6+_9(&3+zdv9svyf@v)#f&h03jt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'users.apps.UsersConfig'
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

ROOT_URLCONF = 'DOEJoseph.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DOEJoseph.wsgi.application'



# Alapértelmezett beállítás (SQLite) lokális fejlesztéshez
default_db_config = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

# A Railway (vagy más szolgáltató) által biztosított DATABASE_URL beolvasása
# Ha létezik, felülírja az alapértelmezett SQLite beállítást.
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    print("Connecting to external Postgres database...") # Ez segít a logokban látni, hogy sikerült-e
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    print("DATABASE_URL not found, using local SQLite.")
    DATABASES = {
        'default': default_db_config
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'hu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL hozzáadása (ez hiányzott)
STATIC_URL = '/static/'

# STATICFILES_DIRS - csak akkor add hozzá, ha a könyvtár létezik
static_dir = os.path.join(BASE_DIR, "static")
if os.path.exists(static_dir):
    STATICFILES_DIRS = [static_dir]
else:
    
    print(f"Figyelem: A static könyvtár nem létezik: {static_dir}")
    STATICFILES_DIRS = []

# DEFAULT_AUTO_FIELD kommentből kivétele
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'user'

MEDIA_URL = '/pictures/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'pictures')
