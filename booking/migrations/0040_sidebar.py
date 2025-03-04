# Generated by Django 5.0.3 on 2024-06-12 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0039_crudoperations_delete_flight_crudoperations'),
    ]

    operations = [
        migrations.CreateModel(
            name='sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=100)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='booking.sidebar')),
            ],
        ),
    ]
