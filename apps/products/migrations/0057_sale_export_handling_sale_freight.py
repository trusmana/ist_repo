# Generated by Django 4.0.2 on 2022-10-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_produk_jenis_produk'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='export_handling',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='freight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True),
        ),
    ]