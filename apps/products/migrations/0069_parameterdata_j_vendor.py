# Generated by Django 4.0.2 on 2022-11-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0068_parameterdata_min_agent_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterdata',
            name='j_vendor',
            field=models.CharField(choices=[('1', 'SATU'), ('2', 'DUA'), ('3', 'TIGA')], max_length=20, null=True),
        ),
    ]
