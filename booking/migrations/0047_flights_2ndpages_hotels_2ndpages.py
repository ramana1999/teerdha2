# Generated by Django 5.0.6 on 2024-06-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0046_delete_cabs_offerscrudoperations'),
    ]

    operations = [
        migrations.CreateModel(
            name='flights_2ndpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=100)),
                ('inserturl', models.URLField()),
                ('updateurl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='hotels_2ndpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=100)),
                ('inserturl', models.URLField()),
                ('updateurl', models.URLField()),
            ],
        ),
    ]
