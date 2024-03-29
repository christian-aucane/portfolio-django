# Generated by Django 5.0.1 on 2024-01-24 10:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Processed')),
                ('processed_at', models.DateTimeField(blank=True, null=True, verbose_name='Processed at')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archived')),
                ('archived_at', models.DateTimeField(blank=True, null=True, verbose_name='Archived at')),
            ],
            options={
                'verbose_name': 'Contact Thread',
                'verbose_name_plural': 'Contact Threads',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=255, verbose_name='Sender')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages',
                                             to='contact.contactthread', verbose_name='Thread')),
            ],
            options={
                'verbose_name': 'Contact Message',
                'verbose_name_plural': 'Contact Messages',
                'ordering': ['created_at'],
            },
        ),
    ]
