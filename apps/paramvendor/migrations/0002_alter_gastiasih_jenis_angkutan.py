# Generated by Django 4.0.2 on 2022-11-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paramvendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastiasih',
            name='jenis_angkutan',
            field=models.CharField(blank=True, choices=[('1', 'Airfreight'), ('2', 'Seafreight')], max_length=20, null=True),
        ),
    ]
