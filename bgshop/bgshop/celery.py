from celery import Celery
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bgshop.settings")
app = Celery("bgshop")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()