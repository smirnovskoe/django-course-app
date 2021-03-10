from django.db import models

from lessons.models import Lesson


class Material(models.Model):
    MATERIAL_TYPE = [
        ('theory', 'Theoretical material'),
        ('practice', 'Practical')
    ]

    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='materials/')

    material_type = models.CharField(
        max_length=25,
        choices=MATERIAL_TYPE,
        default='theory',
    )

    lesson = models.ManyToManyField(Lesson, )

    def __str__(self):
        return f'{self.title}'
