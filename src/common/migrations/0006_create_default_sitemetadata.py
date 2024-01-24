from django.db import migrations

from common.models import SiteMetaData


def create_default_site_meta_data(apps, schema_editor):
    SiteMetaData.objects.get_or_create()


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_sitemetadata'),
    ]

    operations = [
        migrations.RunPython(create_default_site_meta_data, reverse_code=migrations.RunPython.noop),
    ]
