# Generated by Django 4.0.2 on 2022-10-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_remove_job_qty_produk_kurs_destinations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='kurs_destinations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_destinastions', to='products.kurs'),
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
    ]