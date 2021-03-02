from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'trainer', 'status', 'date_start', 'date_end', 'publish',)
    list_filter = ("status", "trainer")
    search_fields = ['title', 'trainer']
    prepopulated_fields = {'slug': ('course_name',)}
