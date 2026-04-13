import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn2earn.core.settings")

app = Celery("learn2earn")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
