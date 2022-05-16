#from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'masmed.settings')
app = Celery('masmed', broker='amqps://admin:1234@127.0.0.1:5672/ngonied_host?ssl=true')
print(app.conf.broker_url)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()