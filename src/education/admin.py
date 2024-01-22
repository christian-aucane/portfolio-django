from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'program', 'start_date', 'end_date')
    search_fields = ('school_name', 'program', 'description')
