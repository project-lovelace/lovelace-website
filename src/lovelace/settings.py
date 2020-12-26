import os

# Consult the deployment checklist before deploying to production:
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG")))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition
INSTALLED_APPS = [
    'problems.apps.ProblemsConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_countries',
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

ROOT_URLCONF = 'lovelace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # project-level templates directory
        ],
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

WSGI_APPLICATION = 'lovelace.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    "default": {
          "ENGINE": os.environ.get("SQL_ENGINE"),
            "NAME": os.environ.get("SQL_DATABASE"),
            "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
            "HOST": os.environ.get("SQL_HOST"),
            "PORT": os.environ.get("SQL_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Directory for media files. Mostly used for storing user submitted files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

# Look for static files in the project-level static files directory
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# When running collectstatic in production, put all static files into src/static_prod
STATIC_ROOT = os.path.join(BASE_DIR, 'static_prod')

# When client requests files under projectlovelace.net/static, look for them in STATIC_ROOT
STATIC_URL = '/static_prod/'

# Login URL used especially by @login_required decorator.
LOGIN_URL = '/accounts/login/'

# Redirect users after logging in and logging out
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# SSL/HTTPS settings
USE_SSL = bool(int(os.environ.get("USE_SSL")))
SECURE_SSL_REDIRECT = USE_SSL
SESSION_COOKIE_SECURE = USE_SSL
CSRF_COOKIE_SECURE = USE_SSL

# # More recommended security settings
SECURE_CONTENT_TYPE_NOSNIFF = USE_SSL
SECURE_BROWSER_XSS_FILTER = USE_SSL
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") if USE_SSL else None

# Email server settings
# See: https://docs.djangoproject.com/en/stable/topics/email/

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

# These are used by send_mass_email.py
LOVELACE_FROM_EMAIL = os.environ.get("LOVELACE_FROM_EMAIL")
MAILGUN_API_URL = os.environ.get("MAILGUN_API_URL")
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

# django-registration settings
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window

# Discourse settings.
# See: https://meta.discourse.org/t/sso-example-for-django/14258
DISCOURSE_BASE_URL = 'http://discourse.projectlovelace.net'
DISCOURSE_SSO_SECRET = 'discourse-sso-secret'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(name)s.%(levelname)s (%(pathname)s:%(lineno)d): %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.FileHandler',
            'filename': 'lovelace-django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
