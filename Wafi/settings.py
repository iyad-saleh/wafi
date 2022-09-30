from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gk4y-p)ek1r3jcuxg_(x*#hl%a@#wt_q=dl*h2kic!5+8cq91k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


AUTH_USER_MODEL = 'users.MyUser'
# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',

    'crispy_forms',
    'widget_tweaks',
    'import_export',
    'django_extensions',

    'common',
    'company',
    'account',
    'customer',
    'box',
    'coin',
    'passport',
    'employee',
    'bus',
    'expense',
    'trip',
    'reservation',
    'ked',
    'guest',
    'package',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',


]

ROOT_URLCONF = 'Wafi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.contrib.auth.context_processors.i18n',
                # 'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Wafi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = (
    # ('fr', 'Français'),
    # ('de', 'Deutsch'),
    ('en', _('English')),
    ('ar', _('Arabic')),
)
LANGUAGE_CODE = 'en-us'
LOCALE_PATHS = (
    BASE_DIR / 'locale/',
)
TIME_ZONE = 'Asia/Damascus'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_STORAGE = 'media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": "slate",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}


JAZZMIN_SETTINGS = {

"site_title": "Library Admin",
# Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if abse
"site_header": "Library",
# Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or N
"site_brand": "Library",
# Logo to use for your site, must be present in static files, used for brand on top left
"site_logo": "media/logo.png",
# Logo to use for your site, must be present in static files, used for login form logo (defaul
"login_logo": None,
# Logo to use for login form in dark themes (defaults to login_logo)
"login_logo_dark": None,
# CSS classes that are applied to the logo above
"site_logo_classes": "img-circle",
# Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32
"site_icon": None,
# Welcome text on the login screen
"welcome_sign": "Welcome to the library",
# Copyright on the footer
"copyright": "Eyad Library Ltd",
# The model admin to search from the search bar, search bar omitted if excluded
"search_model": "auth.User",
# Field name on user model that contains avatar ImageField/URLField/Charfield or a callable th
"user_avatar": None,

    "topmenu_links": [
# Url that gets reversed (Permissions can be added)
{"name": "Home", "url": "home"},
# model admin to link to (Permissions checked against model)
{"model": "auth.User"},
# App with dropdown menu to all its models pages (Permissions checked against models)
{"app": "company"},
{"app": "blog"},
    ],

# Additional links to include in the user menu on the top right ("app" url type is not allowed
"usermenu_links": [
    {"name": "Support",
     "url": "https://github.com/farridav/django-jazzmin/issues",
      "new_window":True},
    {"model": "auth.user"}
],

#############
# Side Menu #
#############
# Whether to display the side menu
"show_sidebar": True,
# Whether to aut expand the menu
"navigation_expanded": True,
# Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
# Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
# List of apps (and/or models) to base side menu ordering off of (does not need to contain all
    "order_with_respect_to": ["auth", "blog", "company"],
# Custom links to append to app groups, keyed on app name
    # "custom_links": {
    # "books": [{
    # "name": "Make Messages",
    # "url": "make_messages",
    # "icon": "fas fa-comments",
    # "permissions": ["books.view_book"]
# }]
# },
# Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=
# for the full list of 5.13.0 free icon classes
"icons": {
"auth": "fas fa-users-cog",
"auth.user": "fas fa-user",
"auth.Group": "fas fa-users",
"company.company":"fas fa-box",
"company.companyType":"fas fa-object-group",
"customer.customer":"fas fa-registered",
"coin.coin":"fas fa-coins",
"passport.passport":"fas fa-passport",
"employee.employee":"fas fa-people-carry",
"bus.bus":"fas fa-bus",
"bus.driver":"fas fa-car",
"blog.post":"fas fa-blog",
"box.box":"fas fa-box-open",
"expense.expense":"fas fa-coffee",
"account.account":"fas fa-cash-register",
"ked.journal":"fas fa-journal-whills",
"ked.ked":"fas fa-address-book",
},
# Icons that are used when one is not manually specified
"default_icon_parents": "fas fa-chevron-circle-right",
"default_icon_children": "fas fa-circle",
#################
# Related Modal #
#################
# Use modals instead of popups
"related_modal_active": True,
"show_ui_builder": False,

# "language_chooser": True,

"changeform_format": "carousel",


}