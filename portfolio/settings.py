import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['localhost', '127.0.0.1']),
)

# Lire .env si présent (dev local)
environ.Env.read_env(BASE_DIR / '.env', overwrite=True)

SECRET_KEY = env('SECRET_KEY', default='django-insecure-dev-key-change-me')
DEBUG      = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS') + ['.railway.app', '.up.railway.app', '.onrender.com']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'portfolio_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# ── STATIC (WhiteNoise) ───────────────────────────────────
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ── EMAIL (Gmail SMTP) ───────────────────────────────────
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True
EMAIL_HOST_USER     = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL  = env('EMAIL_HOST_USER', default='noreply@portfolio.dev')
CONTACT_EMAIL       = env('CONTACT_EMAIL', default=EMAIL_HOST_USER)

# ── SECURITY ─────────────────────────────────────────────
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
    'https://*.onrender.com',
]
DEFAULT_AUTO_FIELD   = 'django.db.models.BigAutoField'
