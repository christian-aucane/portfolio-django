# Generated by Django 5.0.1 on 2024-01-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_education_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='education_thumbnails/', verbose_name='Thumbnail'),
        ),
    ]