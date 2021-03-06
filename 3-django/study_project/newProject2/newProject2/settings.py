"""
Django settings for newProject2 project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o!ao@mgqq)v25!85d4=wcc5+7@*ka!kvr=(q6iz+!po$u#+nfa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
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

ROOT_URLCONF = 'newProject2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'newProject2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orm_study2',
        'USER': 'liu',
        'PASSWORD': 'lh284259',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# =====================如果没有写下面的session配置就是没有变动django内部没变动的session配置===========================
STATIC_URL = '/static/'
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 将session中的信息默认放置在数据库
# 修改放置的位置

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎设置放在文件中
# SESSION_FILE_PATH = None     # 缓存文件的路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎设置放在缓存里面，缓存是另一个服务器里面
# SESSION_CACHE_ALIAS = 'default'    # 使用缓存的别名（默认内存缓存，也可以设置）
# 缓存在使用的时候要配合django的缓存配置

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db' # 引擎设置为缓存加数据库
SESSION_COOKIE_NAME = 'sessionid'                       # 控制浏览器cookie中session叫什么名字
SESSION_COOKIE_PATH = '/'                               # path=/ 表示在页面的所有的url上都生效
SESSION_COOKIE_DOMAIN = None                            # 设置域名，默认是用的当前的域名
SESSION_COOKIE_SECURE = False                           # 是否HTTPS传输cookie
SESSION_COOKIE_HTTPONLY = True                          # 是否只能通过http传输cookie中的session
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                 # 是否关闭浏览器的时候让session过期
SESSION_SAVE_EVERY_REQUEST = False                      # 是否每次请求都保存session，默认修改之后才保存
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
