# Generated by Django 4.0.2 on 2022-10-13 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_transaksi_commodity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='products',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.produk'),
        ),
    ]
