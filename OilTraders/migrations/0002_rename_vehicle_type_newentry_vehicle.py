# Generated by Django 5.0.7 on 2024-08-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OilTraders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newentry',
            old_name='vehicle_Type',
            new_name='vehicle',
        ),
    ]
