# Generated by Django 4.0.2 on 2022-11-10 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0063_negara_nama_kota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameterdata',
            name='max_airfreight',
        ),
        migrations.RemoveField(
            model_name='parameterdata',
            name='price_high_airfreight',
        ),
    ]
