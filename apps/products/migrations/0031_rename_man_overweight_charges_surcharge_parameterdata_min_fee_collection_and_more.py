# Generated by Django 4.0.2 on 2022-10-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_remove_parameterdata_max_fuel_surcharge_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameterdata',
            old_name='man_overweight_charges_surcharge',
            new_name='min_fee_collection',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_admin_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_airfreight_charges',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_akses_bandara_inspeksi',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_awb_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_delivey_to_hera',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_forklift_for_heavy_cargo',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_handling_charges_sl',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_handling_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_pjkp2u_dps_dil_at_cost',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_pjkp2u_sin_dps_at_cost',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_storage_mcl_e_0389249_at_cost',
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='admin_high_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='fee_high_collection',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_airfreight_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_akses_bandara_inspeksi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_awb_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_custom_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_delivey_to_hera',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_forklift_for_heavy_cargo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_ground_handling',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_handling_charges_sl',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_handling_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_overweight_charges_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_pjkp2u_dps_dil_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_pjkp2u_sin_dps_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_storage_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_storage_mcl_e_0389249_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
