import datetime

from core.celery import app
from . import models
from .constants import EMAIL_MESSAGES
from .services import send


@app.task
def update_to_start_and_notify_person():
    """Course status update to: started"""
    course_started = set()

    for course in models.Course.objects.filter(date_start__lte=datetime.date.today(),
                                               date_end__gte=datetime.date.today()):  # course start
        if course.status == course.CourseStatus.DIDNT_START:
            course.status = models.Course.CourseStatus.START
            course.save()

            course_started.add((
                course.trainer.email,
                course.course_name,
                EMAIL_MESSAGES[models.Course.CourseStatus.START])
            )

    for email, course_name, msg in course_started:
        send(email, course_name, msg)


@app.task
def update_to_ended_and_notify_person():
    """"""
    course_ended = set()

    for course in models.Course.objects.filter(date_end__lt=datetime.date.today()):  # course end
        if course.status == course.CourseStatus.START:
            course.status = models.Course.CourseStatus.ENDED
            course.save()

            course_ended.add((
                course.trainer.email,
                course.course_name,
                EMAIL_MESSAGES[models.Course.CourseStatus.ENDED])
            )

    for email, course_name, msg in course_ended:
        send(email, course_name, msg)
