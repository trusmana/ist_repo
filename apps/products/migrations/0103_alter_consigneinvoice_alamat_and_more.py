# Generated by Django 4.0.2 on 2022-12-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0102_addresinvoice_consigneinvoice_ddpinvoice_terminvoice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consigneinvoice',
            name='alamat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consigneinvoice',
            name='kota',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consigneinvoice',
            name='telepon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shipperinvoice',
            name='alamat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipperinvoice',
            name='kota',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shipperinvoice',
            name='telepon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
