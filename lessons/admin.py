from django.contrib import admin

from . import models


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'duration', 'date_start', 'status', 'course',)
    list_filter = ("course",)
    search_fields = ['lesson_name', 'course']


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('lesson',)
