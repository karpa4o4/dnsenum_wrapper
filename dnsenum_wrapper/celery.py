import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dnsenum_wrapper.settings')

app = Celery('dnsenum_wrapper', broker='amqp://guest:guest@rabbitmq')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()