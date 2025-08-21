import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','farmsphere.settings')
app=Celery('farmsphere')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
