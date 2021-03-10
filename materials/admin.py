from django.contrib import admin

from . import models


@admin.register(models.Material)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'material_type')
