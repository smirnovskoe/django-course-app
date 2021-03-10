from django.db import models
from django.db.models.signals import post_save
from mdeditor.fields import MDTextField

from courses.models import Course


class Lesson(models.Model):
    STATUS = (
        ("Didn't start", "Didn't start",),
        ('In progress', "In progress",),
        ('Ended', 'Ended',),
    )

    lesson_name = models.CharField(max_length=255)
    duration = models.TimeField()
    # add published
    date_start = models.DateTimeField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=25,
        choices=STATUS,
        default="Didn't start",
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.lesson_name}'


class Plan(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    body = MDTextField()

    def __str__(self):
        return f'{self.lesson}'


# Django signals

def post_lesson_created_signal(sender, instance, created, **kwargs):
    if created:
        Plan.objects.create(lesson=instance)


post_save.connect(post_lesson_created_signal, sender=Lesson)
