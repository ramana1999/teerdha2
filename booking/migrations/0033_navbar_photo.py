# Generated by Django 4.2.7 on 2024-05-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0032_hotel_cards_book_now_alter_hotel_cards_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='photo',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
