from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import (
    text,
    timezone
)
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Course(models.Model):
    class CourseStatus(models.TextChoices):
        DIDNT_START = "Didn't start", _("DIDNT")
        START = 'Start', _('START')
        ENDED = 'Ended', _('ENDED')

    course_name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='course_images/', default='course_images/default.png')
    slug = models.SlugField(max_length=255, unique=True)

    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, )

    description = models.TextField(blank=True, null=True)

    date_start = models.DateField()
    date_end = models.DateField()

    publish = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=CourseStatus.choices,
        default=CourseStatus.DIDNT_START,
    )

    class Meta:
        verbose_name_plural = "Courses"

    def get_course_status(self, current_date):
        """Get course status"""
        if self.date_start <= current_date <= self.date_end:
            return self.CourseStatus.START
        elif self.date_end > current_date:
            return self.CourseStatus.ENDED

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.course_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.course_name}'
