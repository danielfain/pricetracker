import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricetracker.settings")

app = Celery("pricetracker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update-item-prices": {
        "task": "tracker.tasks.update_prices",
        "schedule": 60.0,
    }
}