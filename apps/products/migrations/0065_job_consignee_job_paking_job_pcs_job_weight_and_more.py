# Generated by Django 4.0.2 on 2022-11-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_remove_parameterdata_max_airfreight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='consignee',
            field=models.CharField(blank=True, help_text='Gasti asih caraka', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='paking',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Gasti asih caraka', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pcs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Gasti asih caraka', max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Gasti asih caraka', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='admin_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='airfreight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='akses_bandara_inspeksi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='awb_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='custom_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='delivey_to_hera',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='fee_collection',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='forklift_for_heavy_cargo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='fuel_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ground_handling',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='gst_zero_rated',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='handling_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='handling_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Dili', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='import_handling_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='insurance_security_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Freight', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='overweight_charges_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pjkp2u_dps_dil_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pjkp2u_sin_dps_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='storage_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='storage_mcl_e_0389249_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Solid', max_digits=12, null=True),
        ),
    ]
