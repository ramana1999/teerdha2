# Generated by Django 5.0.3 on 2024-03-21 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_axis_offer_axis_offer1_axis_policy_cards_faqitem_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='axis_offer',
            new_name='hotel_axisoffer',
        ),
        migrations.RenameModel(
            old_name='axis_offer1',
            new_name='hotel_axisoffer1',
        ),
        migrations.RenameModel(
            old_name='axis_policy',
            new_name='hotel_axispolicy',
        ),
        migrations.RenameModel(
            old_name='cards',
            new_name='hotel_cards',
        ),
        migrations.RenameModel(
            old_name='sbi_offer',
            new_name='hotel_federaloffer',
        ),
        migrations.RenameModel(
            old_name='hsbc_offer1',
            new_name='hotel_federaloffer1',
        ),
        migrations.RenameModel(
            old_name='federal_policy',
            new_name='hotel_federalpolicy',
        ),
        migrations.RenameModel(
            old_name='hsbc_offer',
            new_name='hotel_hsbcoffer',
        ),
        migrations.RenameModel(
            old_name='federal_offer1',
            new_name='hotel_hsbcoffer1',
        ),
        migrations.RenameModel(
            old_name='sbi_policy',
            new_name='hotel_hsbcpolicy',
        ),
        migrations.RenameModel(
            old_name='federal_offer',
            new_name='hotel_icicioffer',
        ),
        migrations.RenameModel(
            old_name='icici_offer1',
            new_name='hotel_icicioffer1',
        ),
        migrations.RenameModel(
            old_name='icici_policy',
            new_name='hotel_icicipolicy',
        ),
        migrations.RenameModel(
            old_name='icici_offer',
            new_name='hotel_sbioffer',
        ),
        migrations.RenameModel(
            old_name='sbi_offer1',
            new_name='hotel_sbioffer1',
        ),
        migrations.RenameModel(
            old_name='hsbc_policy',
            new_name='hotel_sbipolicy',
        ),
        migrations.RenameField(
            model_name='hotel_hsbcpolicy',
            old_name='cnt',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='hotel_hsbcpolicy',
            old_name='cnt1',
            new_name='data1',
        ),
        migrations.RenameField(
            model_name='hotel_hsbcpolicy',
            old_name='cnt2',
            new_name='data2',
        ),
        migrations.RenameField(
            model_name='hotel_hsbcpolicy',
            old_name='cnt3',
            new_name='data3',
        ),
        migrations.RenameField(
            model_name='hotel_hsbcpolicy',
            old_name='cnt4',
            new_name='data4',
        ),
        migrations.RenameField(
            model_name='hotel_sbipolicy',
            old_name='data',
            new_name='cnt',
        ),
        migrations.RenameField(
            model_name='hotel_sbipolicy',
            old_name='data1',
            new_name='cnt1',
        ),
        migrations.RenameField(
            model_name='hotel_sbipolicy',
            old_name='data2',
            new_name='cnt2',
        ),
        migrations.RenameField(
            model_name='hotel_sbipolicy',
            old_name='data3',
            new_name='cnt3',
        ),
        migrations.RenameField(
            model_name='hotel_sbipolicy',
            old_name='data4',
            new_name='cnt4',
        ),
        migrations.AlterModelTable(
            name='hotel_axisoffer',
            table='hotel_axisoffer',
        ),
        migrations.AlterModelTable(
            name='hotel_axisoffer1',
            table='hotel_axisoffer1',
        ),
        migrations.AlterModelTable(
            name='hotel_axispolicy',
            table='hotel_axispolicy',
        ),
        migrations.AlterModelTable(
            name='hotel_federaloffer',
            table='hotel_federaloffer',
        ),
        migrations.AlterModelTable(
            name='hotel_federaloffer1',
            table='hotel_federaloffer1',
        ),
        migrations.AlterModelTable(
            name='hotel_federalpolicy',
            table='hotel_federalpolicy',
        ),
        migrations.AlterModelTable(
            name='hotel_hsbcoffer',
            table='hotel_hsbcoffer',
        ),
        migrations.AlterModelTable(
            name='hotel_hsbcoffer1',
            table='hotel_hsbcoffer1',
        ),
        migrations.AlterModelTable(
            name='hotel_hsbcpolicy',
            table='hotel_hsbcpolicy',
        ),
        migrations.AlterModelTable(
            name='hotel_icicioffer',
            table='hotel_icicioffer',
        ),
        migrations.AlterModelTable(
            name='hotel_icicioffer1',
            table='hotel_icicioffer1',
        ),
        migrations.AlterModelTable(
            name='hotel_icicipolicy',
            table='hotel_icicipolicy',
        ),
        migrations.AlterModelTable(
            name='hotel_sbioffer',
            table='hotel_sbioffer',
        ),
        migrations.AlterModelTable(
            name='hotel_sbioffer1',
            table='hotel_sbioffer1',
        ),
        migrations.AlterModelTable(
            name='hotel_sbipolicy',
            table='hotel_sbipolicy',
        ),
    ]
