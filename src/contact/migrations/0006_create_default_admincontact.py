from django.db import migrations

from contact.models import AdminContact


def create_default_admin_contact(apps, schema_editor):
    AdminContact.objects.get_or_create()


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_admincontact_admin_email_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_admin_contact, reverse_code=migrations.RunPython.noop),
    ]
