import os
from pathlib import Path

# プロジェクトのルートディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティ設定（開発用）
SECRET_KEY = 'django-insecure-your-secret-key-here'

# ★重要：DEBUGはTrueにしておく（画像を表示するため）
DEBUG = True

# 許可するホスト名
ALLOWED_HOSTS = []

# インストールされているアプリ
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'triplog', # あなたが作ったアプリ
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', # メディアファイルを扱うため
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# データベース（SQLite）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワードバリデーション
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# 言語とタイムゾーンの設定（日本用に変更）
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# 静的ファイル（CSS/JavaScript）の設定
STATIC_URL = 'static/'

# --- メディアファイル（画像）の保存設定 ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# デフォルトのプライマリキーの型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- ?? ログイン・ログアウト後のリダイレクト設定 ---
# ログインが成功したらトップ（地図）へ
LOGIN_REDIRECT_URL = '/'
# ログアウトしたらログイン画面へ
# 一度にアップロードできるファイルの最大数（デフォルトは1000）
DATA_UPLOAD_MAX_NUMBER_FILES = 1000
LOGOUT_REDIRECT_URL = '/accounts/login/'