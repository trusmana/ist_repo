# Generated by Django 4.0.2 on 2022-12-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0104_remove_invoice_ddp_remove_invoice_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'NonAktif'), ('1', 'Aktif')], default=0, max_length=20, null=True),
        ),
    ]
