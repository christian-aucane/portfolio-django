# Generated by Django 5.0.1 on 2024-01-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_education_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='thumbnail',
            field=models.ImageField(upload_to='education_thumbnails/', verbose_name='Thumbnail'),
        ),
    ]