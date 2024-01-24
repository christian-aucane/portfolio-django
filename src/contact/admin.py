from django.contrib import admin

from contact.models import ContactMessage, ContactThread


class ContactMessageInline(admin.TabularInline):
    model = ContactMessage
    extra = 0
    readonly_fields = ('sender', 'created_at', 'message')


@admin.register(ContactThread)
class ContactThreadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'processed_at', 'archived_at', 'is_processed', 'is_archived')
    list_editable = ('is_processed', 'is_archived')
    inlines = [ContactMessageInline]
    readonly_fields = ('name', 'email', 'subject', 'created_at', 'processed_at', 'archived_at')
