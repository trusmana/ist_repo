# Generated by Django 4.0.2 on 2022-11-17 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0078_merge_0068_job_jenis_0077_alter_transaksi_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jasapengiriman',
            name='nilai_kurs',
        ),
        migrations.RemoveField(
            model_name='job',
            name='agent_fee',
        ),
        migrations.RemoveField(
            model_name='job',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='job',
            name='biaya_peb',
        ),
        migrations.RemoveField(
            model_name='job',
            name='blfee',
        ),
        migrations.RemoveField(
            model_name='job',
            name='cbm',
        ),
        migrations.RemoveField(
            model_name='job',
            name='consignee',
        ),
        migrations.RemoveField(
            model_name='job',
            name='custom_learance_fee_handling',
        ),
        migrations.RemoveField(
            model_name='job',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='job',
            name='emergency_situation',
        ),
        migrations.RemoveField(
            model_name='job',
            name='express_wordwide_nondoc',
        ),
        migrations.RemoveField(
            model_name='job',
            name='fuel_surcharge_dhl',
        ),
        migrations.RemoveField(
            model_name='job',
            name='heavy_weight_surcharge',
        ),
        migrations.RemoveField(
            model_name='job',
            name='jenis',
        ),
        migrations.RemoveField(
            model_name='job',
            name='no_invoice_sl_2',
        ),
        migrations.RemoveField(
            model_name='job',
            name='no_invoice_sl_3',
        ),
        migrations.RemoveField(
            model_name='job',
            name='paking',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pcs',
        ),
        migrations.RemoveField(
            model_name='job',
            name='transit_charge',
        ),
        migrations.RemoveField(
            model_name='job',
            name='transportations_charge',
        ),
        migrations.RemoveField(
            model_name='job',
            name='twentyft',
        ),
        migrations.RemoveField(
            model_name='job',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='negara',
            name='cu',
        ),
        migrations.RemoveField(
            model_name='negara',
            name='nama_kota',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='j_vendor',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_agent_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_custom_learance_fee_handling',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_delivery',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_emergency_situation',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_express_wordwide_nondoc',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_fuel_surcharge_dhl',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_heavy_weight_surcharge',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_paking',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_pcs',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='min_weight',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_agent_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_custom_learance_fee_handling',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_delivery',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_emergency_situation',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_express_wordwide_nondoc',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_fuel_surcharge_dhl',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_heavy_weight_surcharge',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_agent_fee',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_custom_learance_fee_handling',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_delivery',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_emergency_situation',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_express_wordwide_nondoc',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_fuel_surcharge_dhl',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_heavy_weight_surcharge',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_paking',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_pcs',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_weight',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_paking',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_pcs',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_weight',
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='max_airfreight',
            field=models.FloatField(blank=True, help_text='Freigh Solution', null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='price_high_airfreight',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Freigh Solution', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='admin_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='airfreight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='akses_bandara_inspeksi',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='awb_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='custom_clearance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='delivey_to_hera',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='fee_collection',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='forklift_for_heavy_cargo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='fuel_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ground_handling',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='gst_zero_rated',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='handling_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='handling_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='import_handling_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='insurance_security_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='no_invoice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='overweight_charges_surcharge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pjkp2u_dps_dil_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pjkp2u_sin_dps_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='storage_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='storage_mcl_e_0389249_at_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='jenis_produk',
            field=models.CharField(blank=True, choices=[('1', 'Airfreight'), ('2', 'Seafreight')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='jumlah_vendor',
            field=models.CharField(blank=True, choices=[('1', 'SATU'), ('2', 'DUA'), ('3', 'TIGA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='kurs_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_kurs', to='products.kurs'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='kurs_through',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_trough', to='products.kurs'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='origin_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_v1', to='products.jasapengiriman'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='point_dua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_dua', to='products.negara'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='point_satu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_satu', to='products.negara'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='through_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Through_v2', to='products.jasapengiriman'),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
