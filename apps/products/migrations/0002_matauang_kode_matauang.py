# Generated by Django 4.0.2 on 2022-09-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matauang',
            name='kode_matauang',
            field=models.CharField(max_length=5, null=True),
        ),
    ]