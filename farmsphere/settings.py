
# FarmSphere settings - human configured - tejaswar 2025
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','dev-not-for-prod-'+'x'*20)
DEBUG = os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.gis',
    'apps.farms','apps.crops','apps.soil_iot','apps.weather','apps.mandi_pricing','apps.coldchain',
    'apps.logistics','apps.subsidies','apps.fpo','apps.inventory','apps.payments','apps.advisory',
    'apps.disease_ai','apps.land_records','apps.analytics',
]
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware']
ROOT_URLCONF='farmsphere.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request']}}]
WSGI_APPLICATION='farmsphere.wsgi.application'
DATABASES={'default':{'ENGINE': os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME': os.environ.get('DB_NAME','farmsphere'),'USER': os.environ.get('DB_USER','farmsphere'),'PASSWORD': os.environ.get('DB_PASSWORD','farmsphere'),'HOST': os.environ.get('DB_HOST','localhost')}}
# fallback for demo / CI without postgres : better-sqlite3 analogy via sqlite
if os.environ.get('USE_SQLITE','0')=='1':
    DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CACHES={'default':{'BACKEND':'django.core.cache.backends.redis.RedisCache','LOCATION': os.environ.get('REDIS_URL','redis://127.0.0.1:6379/1')}}
CELERY_BROKER_URL=os.environ.get('CELERY_BROKER','redis://127.0.0.1:6379/0')
STATIC_URL='/static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
