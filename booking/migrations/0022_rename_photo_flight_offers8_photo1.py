# Generated by Django 5.0.3 on 2024-04-08 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0021_alter_flight_offers8_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight_offers8',
            old_name='photo',
            new_name='photo1',
        ),
    ]
