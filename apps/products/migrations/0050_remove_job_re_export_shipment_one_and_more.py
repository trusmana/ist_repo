# Generated by Django 4.0.2 on 2022-10-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0049_rename_re_export_shipment_pcs_job_re_export_shipment_two_pcs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_one',
        ),
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_one_pcs',
        ),
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_one_qty',
        ),
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_two',
        ),
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_two_pcs',
        ),
        migrations.RemoveField(
            model_name='job',
            name='re_export_shipment_two_qty',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_one',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_one_pcs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_one_qty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_two',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_two_pcs',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='re_export_shipment_two_qty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]
