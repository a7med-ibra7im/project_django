# Generated by Django 5.0.1 on 2024-01-30 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='slug',
            new_name='PRDSlug',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
    ]
