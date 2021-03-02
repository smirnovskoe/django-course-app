from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import (
    text,
    timezone
)

User = get_user_model()


class Course(models.Model):
    STATUS = (
        (0, "Didn't start"),
        (1, 'Start'),
        (3, 'Ended'),
    )

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

    status = models.IntegerField(
        choices=STATUS,
        default=0,
    )

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.course_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.course_name}'
