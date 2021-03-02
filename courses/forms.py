from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from . import models

User = get_user_model()


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = (
            'course_name',
            'description',
            'date_start',
            'date_end',
            'status',
        )
        exclude = ('trainer',)


class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=255)
    date_start = forms.DateField()
    date_end = forms.DateField()
    status = forms.IntegerField()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
