"""
Django settings for galabill project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import json
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
SETTINGS_DIR = os.path.join(BASE_DIR, 'galabill')
SETTINGS_FILE = os.path.join(SETTINGS_DIR, 'settings_attr.json')

with open(SETTINGS_FILE) as f:

    settings_json = json.loads(f.read())
if settings_json['debug']['mode'] == 'dev':
    # debug True
    # SECURITY WARNING: keep the secret key used in production secret!

    SECRET_KEY = settings_json['base']['key']
    # SECURITY WARNING: don't run with debug turned on in production!

    DEBUG = True
    DEPLOY = False

    ALLOWED_HOSTS = '*'

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'storages',
        'authapp',
        'baseapp',
        'object',
        'notice',
        'relation',
        'paypal.standard.ipn',
        'debug_toolbar',
    ]
    # django debug-toolbar
    INTERNAL_IPS = ('127.0.0.1',)

    # For Sandbox account-------------------------------------------------------------------
    PAYPAL_TEST = True
    # For PAYPAL PDT------------------------------------------------------------------------
    # PAYPAL_IDENTITY_TOKEN = '_RTtiajy1U_SW7WO_iPEzawd_vsej2iO5GSSxfBs2LmjjDwEHUApVfCCzmy'
    # installed_apps : 'paypal.standard.ipn',
    BUSINESS = "ghdalsrn2sell@gmail.com"

    SITE_ID = 1

    WSGI_APPLICATION = 'galabill.wsgi.application'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # django debug-toolbar
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ROOT_URLCONF = 'galabill.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
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

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # Authentication Backend
    AUTHENTICATION_BACKENDS = [
        # 'authapp.backends.EmailOrUsernameAuthBackend',
        'django.contrib.auth.backends.ModelBackend',

    ]
    #### Static settings
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')#이 폴더가 없으면 만들어질 것이다.

    #### Media settings
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media_dir')

    '''
    # -------------------------------------------------------------------
    # Static settings1
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = settings_json['cdn']['aws']['aws_access_key_id']
    AWS_SECRET_ACCESS_KEY = settings_json['cdn']['aws']['aws_secret_access_key']
    AWS_STORAGE_BUCKET_NAME = settings_json['cdn']['aws']['aws_storage_bucket_name']
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': settings_json['cdn']['aws']['aws_s3_object_parameters']['cachecontrol'],
    }

    AWS_S3_CUSTOM_DOMAIN = settings_json['cdn']['aws']['aws_s3_custom_domain']
    AWS_S3_SCHEME = 'https://'
    # Static Setting
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    # Media Setting
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

    '''
    # -------------------------------------------------------------------

    # 이미 사용중인 이메일로 리센드 할 시의 문제

    SMTPusername = settings_json['ses']['SMTPusername']
    SMTPpassword = settings_json['ses']['SMTPpassword']

    # Email-backend
    EMAIL_BACKEND = settings_json['ses']['email_backend']
    EMAIL_HOST = settings_json['ses']['email_host']
    EMAIL_PORT = 587
    EMAIL_HOST_USER = SMTPusername
    EMAIL_HOST_PASSWORD = SMTPpassword
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = settings_json['ses']['default_from_email']

elif settings_json['debug']['mode'] == 'deploy':
    # debug True
    # SECURITY WARNING: keep the secret key used in production secret!

    SECRET_KEY = settings_json['base']['key']
    # SECURITY WARNING: don't run with debug turned on in production!

    DEBUG = False
    DEPLOY = True

    ALLOWED_HOSTS = '*'

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'storages',
        'authapp',
        'baseapp',
        'object',
        'notice',
        'relation',
        'paypal.standard.ipn',
    ]

    # For Sandbox account-------------------------------------------------------------------
    PAYPAL_TEST = False
    # For PAYPAL PDT------------------------------------------------------------------------
    # PAYPAL_IDENTITY_TOKEN = '_RTtiajy1U_SW7WO_iPEzawd_vsej2iO5GSSxfBs2LmjjDwEHUApVfCCzmy'
    # installed_apps : 'paypal.standard.ipn',
    BUSINESS = "idigmh397@gmail.com"

    SITE_ID = 1

    WSGI_APPLICATION = 'galabill.wsgi.application'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'galabill.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
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

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': settings_json['database']['default']['engine'],
            'NAME': settings_json['database']['default']['name'],
            'USER': settings_json['database']['default']['user'],
            'PASSWORD': settings_json['database']['default']['password'],
            'HOST': settings_json['database']['default']['host'],
            'PORT': settings_json['database']['default']['port'],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
                'use_unicode': True,
            }
        }
    }
    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # Authentication Backend
    AUTHENTICATION_BACKENDS = [
        'authapp.backends.EmailOrUsernameAuthBackend',
        # 'django.contrib.auth.backends.ModelBackend',
    ]
    # -------------------------------------------------------------------
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = settings_json['cdn']['aws']['aws_access_key_id']
    AWS_SECRET_ACCESS_KEY = settings_json['cdn']['aws']['aws_secret_access_key']
    AWS_STORAGE_BUCKET_NAME = settings_json['cdn']['aws']['aws_storage_bucket_name']
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': settings_json['cdn']['aws']['aws_s3_object_parameters']['cachecontrol'],
    }

    AWS_S3_CUSTOM_DOMAIN = settings_json['cdn']['aws']['aws_s3_custom_domain']
    AWS_S3_SCHEME = 'https://'
    # Static Setting
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    # Media Setting
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

    # -------------------------------------------------------------------

    # 이미 사용중인 이메일로 리센드 할 시의 문제

    SMTPusername = settings_json['ses']['SMTPusername']
    SMTPpassword = settings_json['ses']['SMTPpassword']

    # Email-backend
    EMAIL_BACKEND = settings_json['ses']['email_backend']
    EMAIL_HOST = settings_json['ses']['email_host']
    EMAIL_PORT = 587
    EMAIL_HOST_USER = SMTPusername
    EMAIL_HOST_PASSWORD = SMTPpassword
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = settings_json['ses']['default_from_email']
elif settings_json['debug']['mode'] == 'deploy_admin':
    # debug True
    # SECURITY WARNING: keep the secret key used in production secret!

    SECRET_KEY = settings_json['base']['key']
    # SECURITY WARNING: don't run with debug turned on in production!

    DEBUG = True
    DEPLOY = True

    ALLOWED_HOSTS = '*'

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'storages',
        'authapp',
        'baseapp',
        'object',
        'notice',
        'relation',
        'paypal.standard.ipn',
        'debug_toolbar',
    ]
    # django debug-toolbar
    INTERNAL_IPS = ('127.0.0.1',)

    # For Sandbox account-------------------------------------------------------------------
    PAYPAL_TEST = True
    # For PAYPAL PDT------------------------------------------------------------------------
    # PAYPAL_IDENTITY_TOKEN = '_RTtiajy1U_SW7WO_iPEzawd_vsej2iO5GSSxfBs2LmjjDwEHUApVfCCzmy'
    # installed_apps : 'paypal.standard.ipn',
    BUSINESS = "ghdalsrn2sell@gmail.com"

    SITE_ID = 1

    WSGI_APPLICATION = 'galabill.wsgi.application'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # django debug-toolbar
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ROOT_URLCONF = 'galabill.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
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

    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': settings_json['database']['default']['engine'],
            'NAME': settings_json['database']['default']['name'],
            'USER': settings_json['database']['default']['user'],
            'PASSWORD': settings_json['database']['default']['password'],
            'HOST': settings_json['database']['default']['host'],
            'PORT': settings_json['database']['default']['port'],
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
                'use_unicode': True,
            }
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # Authentication Backend
    AUTHENTICATION_BACKENDS = [
        # 'authapp.backends.EmailOrUsernameAuthBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = settings_json['cdn']['aws']['aws_access_key_id']
    AWS_SECRET_ACCESS_KEY = settings_json['cdn']['aws']['aws_secret_access_key']
    AWS_STORAGE_BUCKET_NAME = settings_json['cdn']['aws']['aws_storage_bucket_name']
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': settings_json['cdn']['aws']['aws_s3_object_parameters']['cachecontrol'],
    }

    AWS_S3_CUSTOM_DOMAIN = settings_json['cdn']['aws']['aws_s3_custom_domain']
    AWS_S3_SCHEME = 'https://'
    # Static Setting
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    # Media Setting
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

    # -------------------------------------------------------------------

    # 이미 사용중인 이메일로 리센드 할 시의 문제

    SMTPusername = settings_json['ses']['SMTPusername']
    SMTPpassword = settings_json['ses']['SMTPpassword']

    # Email-backend
    EMAIL_BACKEND = settings_json['ses']['email_backend']
    EMAIL_HOST = settings_json['ses']['email_host']
    EMAIL_PORT = 587
    EMAIL_HOST_USER = SMTPusername
    EMAIL_HOST_PASSWORD = SMTPpassword
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = settings_json['ses']['default_from_email']