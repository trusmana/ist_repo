# Generated by Django 4.0.2 on 2022-10-17 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0057_sale_export_handling_sale_freight'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterdatabl',
            name='max_airfreight_sin_dps_dil',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parameterdatabl',
            name='min_airfreight_sin_dps_dil',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
