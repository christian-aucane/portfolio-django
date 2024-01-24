from django.db import migrations

from contact.models import AdminContact


def create_default_admin_contact(apps, schema_editor):
    AdminContact.objects.get_or_create()


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_admincontact'),
    ]

    operations = [
        migrations.RunPython(create_default_admin_contact, reverse_code=migrations.RunPython.noop),
    ]
