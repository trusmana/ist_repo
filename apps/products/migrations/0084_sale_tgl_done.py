# Generated by Django 4.0.2 on 2022-11-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0083_sale_status_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='tgl_done',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
