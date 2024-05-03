# Generated by Django 5.0.1 on 2024-01-25 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_create_default_admincontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='contact.contactthread', verbose_name='Thread'),
        ),
    ]
