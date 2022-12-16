# Generated by Django 4.0.2 on 2022-12-16 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0097_sale_warehouse_charge_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(blank=True, choices=[('1', 'REFF'), ('2', 'CUSTOMER REFF')], max_length=20, null=True)),
                ('jumlahreff', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=20, null=True)),
                ('ref1', models.CharField(blank=True, max_length=20, null=True)),
                ('ref2', models.CharField(blank=True, max_length=20, null=True)),
                ('ref3', models.CharField(blank=True, max_length=20, null=True)),
                ('ref4', models.CharField(blank=True, max_length=20, null=True)),
                ('ref5', models.CharField(blank=True, max_length=20, null=True)),
                ('ref6', models.CharField(blank=True, max_length=20, null=True)),
                ('ref7', models.CharField(blank=True, max_length=20, null=True)),
                ('ref8', models.CharField(blank=True, max_length=20, null=True)),
                ('ref9', models.CharField(blank=True, max_length=20, null=True)),
                ('ref10', models.CharField(blank=True, max_length=20, null=True)),
                ('csref1', models.CharField(blank=True, max_length=20, null=True)),
                ('csref2', models.CharField(blank=True, max_length=20, null=True)),
                ('csref3', models.CharField(blank=True, max_length=20, null=True)),
                ('csref4', models.CharField(blank=True, max_length=20, null=True)),
                ('csref5', models.CharField(blank=True, max_length=20, null=True)),
                ('csref6', models.CharField(blank=True, max_length=20, null=True)),
                ('csref7', models.CharField(blank=True, max_length=20, null=True)),
                ('csref8', models.CharField(blank=True, max_length=20, null=True)),
                ('csref9', models.CharField(blank=True, max_length=20, null=True)),
                ('csref10', models.CharField(blank=True, max_length=20, null=True)),
                ('fkref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sale', verbose_name='fkreff')),
            ],
            options={
                'verbose_name': 'RefCustomer',
                'db_table': 'refcustomer',
            },
        ),
    ]
