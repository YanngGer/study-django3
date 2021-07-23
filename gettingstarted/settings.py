import datetime
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 快速导入模块
sys.path.insert(0, BASE_DIR / 'user')

SECRET_KEY = 'django-insecure-kx@#vqngmz0n(_$w(&(eg-=*%20g6*kuexku@@v-!fy_7u*^n='

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'user',
    'gateway',
]

MIDDLEWARE = [
    # 跨域配置
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS跨域设置
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'gettingstarted.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'gettingstarted.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "yg",
        'HOST': 'localhost',
        "USER": "root",
        "PASSWORD": "admin123456",
    }
}

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

REST_FRAMEWORK = {
    # 接口访问权限
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 新版的restframework生产API文档需要指定默认schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    # 认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # 过滤
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 限流
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',  # 每分钟可以请求两次
        'user': '5/minute'  # 每分钟可以请求五次
    },
    # 异常
    'EXCEPTION_HANDLER': 'gettingstarted.config.exception_handler'
}
# 自定义登录认证
AUTHENTICATION_BACKENDS = ("gettingstarted.config.UserAuthBackend",)

JWT_AUTH = {
    # 手动设置登入认证的时候的返回值
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'gettingstarted.config.jwt_response_payload_handler',
    # 过期时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    # 指定返回响应的格式
    'JWT_AUTH_COOKIE': 'Bearer'
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

MEDIA_URL = '/upload/'
MEDIA_ROOT = BASE_DIR / 'upload'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# 让自定义用户模型生效
AUTH_USER_MODEL = 'user.User'
# 日志
BASE_LOG_DIR = BASE_DIR / 'upload/logs'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(levelname)s]''[%(filename)s:%(lineno)d][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s]%(message)s'
        },

    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_LOG_DIR / 'info.log',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 3,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_LOG_DIR / 'error.log',
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        }

    },
    'loggers': {
        'info': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
        'warn': {
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
        }
    }

}
