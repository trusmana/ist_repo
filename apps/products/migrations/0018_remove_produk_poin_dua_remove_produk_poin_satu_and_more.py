# Generated by Django 4.0.2 on 2022-10-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_negara_singkatan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='poin_dua',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='poin_satu',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='poin_tiga',
        ),
        migrations.AddField(
            model_name='produk',
            name='point_dua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_dua', to='products.jasapengiriman'),
        ),
        migrations.AddField(
            model_name='produk',
            name='point_satu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_satu', to='products.jasapengiriman'),
        ),
        migrations.AddField(
            model_name='produk',
            name='point_tiga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='point_tiga', to='products.jasapengiriman'),
        ),
    ]
