# Generated by Django 5.1.2 on 2024-10-29 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_location_lan_location_lon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='ip',
            new_name='ip_address',
        ),
    ]
