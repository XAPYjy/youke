"""
Django settings for jyoa project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-16x(5!j67@oc3efi@q*3h*xe2qqt8tc0n(g*y_h(qi2_e#l*r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'back_system',
=======
    'yk_models',
    'ykuser',
>>>>>>> 229a5112c2263ab22daeaae144d896d46ecd0558
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
<<<<<<< HEAD
    'middleware.valid_login',
=======
    'corsheaders.middleware.CorsMiddleware',
>>>>>>> 229a5112c2263ab22daeaae144d896d46ecd0558
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'youke.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'youke.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'youke',
<<<<<<< HEAD
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
=======
        # 'HOST': '47.92.132.161',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
>>>>>>> 229a5112c2263ab22daeaae144d896d46ecd0558
        'CHARSET': 'utf8'
    }
}

<<<<<<< HEAD
=======
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
>>>>>>> 229a5112c2263ab22daeaae144d896d46ecd0558

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

<<<<<<< HEAD

# 静态资源文件
STATIC_URL = '/s/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# 上传的文件存放位置
MEDIA_URL = '/s/m/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')


# 配置缓存方案
CACHES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION':'redis://localhost:6379/0'
    },
    'default':{
        'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION':'cache.dat',
        'TIMEOUT':60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_NAME = 'session_id'
SESSION_COOKIE_AGE = 604800    # 一周有效时长（秒）
SESSION_CACHE_ALIAS = 'redis'  #缓存方案，默认default
=======
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/s/'

# 跨域允许的请求方式
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (  # 允许跨域的请求头，
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

CORS_ALLOW_CREDENTIALS = True  # 跨域请求时，是否携带cookie

CORS_ORIGIN_ALLOW_ALL = True  # 允许所有主机执行跨站点请求

REST_FRAMEWORK = {
    # 重构renderer
    'DEFAULT_RENDERER_CLASSES': (
        'util.renderer.YKrender',
    ),
}
# 配置redis缓存
CACHES = {
     'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://47.92.132.161:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

>>>>>>> 229a5112c2263ab22daeaae144d896d46ecd0558
