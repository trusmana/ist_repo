# Generated by Django 4.0.2 on 2022-09-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_produk_alter_kurs_status_kurs_alter_matauang_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='status',
            field=models.CharField(choices=[('', 'NonAktif'), ('1', 'Aktif')], max_length=20),
        ),
    ]
