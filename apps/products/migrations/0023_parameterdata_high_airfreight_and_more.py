# Generated by Django 4.0.2 on 2022-10-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_parameterdata_max_admin_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterdata',
            name='high_airfreight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parameterdata',
            name='high_handling_charge',
            field=models.FloatField(blank=True, null=True),
        ),
    ]