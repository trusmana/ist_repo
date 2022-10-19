# Generated by Django 4.0.2 on 2022-10-14 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_remove_job_weight_transaksi_qty_transaksi_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='qty',
        ),
        migrations.AddField(
            model_name='produk',
            name='kurs_destinations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_destinastions', to='products.jasapengiriman'),
        ),
        migrations.AddField(
            model_name='produk',
            name='kurs_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_kurs', to='products.jasapengiriman'),
        ),
        migrations.AddField(
            model_name='produk',
            name='kurs_through',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_trough', to='products.jasapengiriman'),
        ),
    ]
