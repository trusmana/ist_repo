# Generated by Django 4.0.2 on 2022-12-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0112_menuinputsale_freight_cost_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuinputsale',
            name='insuranse_pers',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Insurence Persen'),
        ),
        migrations.AlterField(
            model_name='menuinputsale',
            name='insuranse_nilai',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Insurence Price '),
        ),
    ]
