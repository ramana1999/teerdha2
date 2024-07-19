# Generated by Django 4.2.3 on 2024-02-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_home_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('description1', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Hotel_offers',
            },
        ),
    ]
