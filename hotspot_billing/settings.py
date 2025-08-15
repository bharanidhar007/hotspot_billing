import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
    "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "rest_framework","crispy_forms","django_countries",
    "accounts","billing","payments","vouchers","devices","ui",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "hotspot_billing.middleware.CountryDetectMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "hotspot_billing.urls"

TEMPLATES = [
    {
        "BACKEND":"django.template.backends.django.DjangoTemplates",
        "DIRS":[BASE_DIR / "templates"],
        "APP_DIRS":True,
        "OPTIONS":{"context_processors":[
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ],},
    },
]

WSGI_APPLICATION = "hotspot_billing.wsgi.application"

DATABASES = {"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Mapping for EA currencies
CURRENCY_MAP = {"KE":"KES","UG":"UGX","TZ":"TZS","RW":"RWF","ET":"ETB","SS":"SSP"}
SYSTEM_COMMISSION_PERCENT = 5
