# Generated by Django 5.0.3 on 2024-06-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0036_rename_flight_offers_update_flight_offersupdate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='flight_offersupdate',
        ),
    ]
