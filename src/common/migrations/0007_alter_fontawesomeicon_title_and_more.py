# Generated by Django 5.0.1 on 2024-01-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_create_default_sitemetadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fontawesomeicon',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='sitemetadata',
            name='og_image',
            field=models.URLField(blank=True, null=True, verbose_name='OG Image URL'),
        ),
    ]
