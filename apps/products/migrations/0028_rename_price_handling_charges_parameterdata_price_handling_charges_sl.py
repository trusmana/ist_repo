# Generated by Django 4.0.2 on 2022-10-09 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_rename_max_handling_charges_parameterdata_max_handling_charges_sl_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameterdata',
            old_name='price_handling_charges',
            new_name='price_handling_charges_sl',
        ),
    ]
