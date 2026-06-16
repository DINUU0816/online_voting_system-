from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-key'

DEBUG = True

ALLOWED_HOSTS = [
    '10.59.187.145',
    'localhost',
    '127.0.0.1',
]


INSTALLED_APPS = [

    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'voting',
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


ROOT_URLCONF = 'online_voting_system.urls'


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


WSGI_APPLICATION = 'online_voting_system.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "voting/static",
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'




JAZZMIN_SETTINGS = {

    "site_title": " ",

    "site_header": " ",

    "site_brand":" ",

    "welcome_sign": "Welcome to VoteSphere",

    "copyright": "VoteSphere Digital Election Platform",

    "site_logo": "images/votesphere_logo.png",

    "login_logo": "images/votesphere_logo.png",

    "site_logo_classes": "img-circle",
    "site_logo_classes": "img-circle elevation-3",
    "show_ui_builder": False,

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "icons": {
        "auth.User": "fas fa-user",
        "voting.Candidate": "fas fa-user-tie",
        "voting.Vote": "fas fa-vote-yea",
        "voting.ElectionResult": "fas fa-chart-bar",
    },

    "topmenu_links": [

        {
            "name": "View Website",
            "url": "/",
            "new_window": False,
        },

        {
            "model": "auth.User",
        },

        {
            "app": "voting",
        },
    ],
}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'