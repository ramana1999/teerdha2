# Generated by Django 4.2.3 on 2024-02-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='naviagtion_bar',
            name='icon',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
