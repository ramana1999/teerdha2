# Generated by Django 5.0.3 on 2024-03-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_hotel_cards_table_alter_hotel_quary_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_boboffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=100)),
                ('cpncode', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hotel_boboffer',
            },
        ),
        migrations.CreateModel(
            name='hotel_boboffer1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('couponcode', models.CharField(max_length=100)),
                ('offer', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hotel_boboffer1',
            },
        ),
        migrations.CreateModel(
            name='hotel_bobpolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField()),
                ('term1', models.TextField()),
                ('term2', models.TextField()),
                ('term3', models.TextField()),
            ],
            options={
                'db_table': 'hotel_bobpolicy',
            },
        ),
    ]
