from django import forms

from . import models


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = (
            'lesson_name',
            'duration',
            'date_start',
        )


class PlanModelForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = ('body',)
