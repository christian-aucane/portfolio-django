from django.contrib import admin

from .models import AwardCategory, Award


@admin.register(AwardCategory)
class AwardCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    list_editable = ('display_order',)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'display_order')
    search_fields = ('title', 'category__title')
    list_filter = ('category__title',)
    list_editable = ('display_order',)
