# Generated by Django 4.0.2 on 2022-11-29 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0084_sale_tgl_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='tgl_done',
            field=models.DateField(blank=True, null=True),
        ),
    ]