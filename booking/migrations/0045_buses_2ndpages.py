# Generated by Django 5.0.6 on 2024-06-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0044_cabs_offerscrud_dashboard_cabs_secondpage_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='buses_2ndpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=100)),
                ('inserturl', models.URLField()),
                ('updateurl', models.URLField()),
            ],
        ),
    ]
