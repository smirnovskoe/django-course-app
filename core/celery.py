import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_course_status_to_ended_and_notify_person': {
        'task': 'courses.tasks.update_to_ended_and_notify_person',
        'schedule': crontab()
    },
    'update_course_status_to_start_and_notify_person': {
        'task': 'courses.tasks.update_to_start_and_notify_person',
        'schedule': crontab()
    }
}
