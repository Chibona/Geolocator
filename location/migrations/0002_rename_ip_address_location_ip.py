# Generated by Django 5.1.2 on 2024-10-29 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='ip_address',
            new_name='ip',
        ),
    ]
