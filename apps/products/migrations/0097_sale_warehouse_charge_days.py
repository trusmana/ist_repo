# Generated by Django 4.0.2 on 2022-12-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0096_sale_awb_sale_price_freight'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='warehouse_charge_days',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
