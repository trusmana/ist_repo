# Generated by Django 4.0.2 on 2022-10-08 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0021_remove_produk_jasa_pengiriman_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterdata',
            name='max_admin_fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='min_admin_fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('cu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_transaksi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaksi',
                'db_table': 'transaksi',
            },
        ),
        migrations.CreateModel(
            name='Jual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_airfreight', models.FloatField(blank=True, null=True)),
                ('price_airfreight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_insurance_security_surcharge', models.FloatField(blank=True, null=True)),
                ('price_insurance_security_surcharge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_fuel_surcharge', models.FloatField(blank=True, null=True)),
                ('price_fuel_surcharge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_import_handling_charges', models.FloatField(blank=True, null=True)),
                ('price_import_handling_charges', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_gst_zero_rated', models.FloatField(blank=True, null=True)),
                ('price_gst_zero_rated', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_storage_at_cost', models.FloatField(blank=True, null=True)),
                ('price_storage_at_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_pjkp2u_sin_dps_at_cost', models.FloatField(blank=True, null=True)),
                ('price_pjkp2u_sin_dps_at_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_storage_mcl_e_0389249_at_cost', models.FloatField(blank=True, null=True)),
                ('price_storage_mcl_e_0389249_at_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_pjkp2u_dps_dil_at_cost', models.FloatField(blank=True, null=True)),
                ('price_pjkp2u_dps_dil_at_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_airfreight_charges', models.FloatField(blank=True, null=True)),
                ('price_airfreight_charges', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_overweight_charges_surcharge', models.FloatField(blank=True, null=True)),
                ('price_overweight_charges_surcharge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_awb_fee', models.FloatField(blank=True, null=True)),
                ('price_awb_fee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_handling_charges', models.FloatField(blank=True, null=True)),
                ('price_handling_charges', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('tanggal_invoice', models.DateTimeField(auto_now_add=True)),
                ('no_invoice', models.IntegerField(blank=True, null=True)),
                ('currency_ground_handling', models.FloatField(blank=True, null=True)),
                ('price_ground_handling', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_forklift_for_heavy_cargo', models.FloatField(blank=True, null=True)),
                ('price_forklift_for_heavy_cargo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_custom_clearance', models.FloatField(blank=True, null=True)),
                ('price_custom_clearance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_delivey_to_hera', models.FloatField(blank=True, null=True)),
                ('price_delivey_to_hera', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_akses_bandara_inspeksi', models.FloatField(blank=True, null=True)),
                ('price_akses_bandara_inspeksi', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_handling_fee', models.FloatField(blank=True, null=True)),
                ('price_handling_fee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_admin_fee', models.FloatField(blank=True, null=True)),
                ('price_admin_fee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('currency_fee_collection', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('price_fee_collection', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('nilai_kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.kurs')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.produk')),
                ('transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.transaksi')),
            ],
            options={
                'verbose_name': 'Jual',
                'db_table': 'jual',
            },
        ),
    ]
