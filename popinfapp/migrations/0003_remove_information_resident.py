# Generated by Django 5.0.1 on 2024-01-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popinfapp', '0002_information_phone_information_resident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='resident',
        ),
    ]
