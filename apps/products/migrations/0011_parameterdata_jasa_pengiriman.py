# Generated by Django 4.0.2 on 2022-09-29 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_parameterdata_jasapengiriman'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterdata',
            name='jasa_pengiriman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.jasapengiriman'),
        ),
    ]
