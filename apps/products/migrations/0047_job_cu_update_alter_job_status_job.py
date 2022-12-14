# Generated by Django 4.0.2 on 2022-10-15 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0046_job_status_job_job_tanggal_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cu_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_jobup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='status_job',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Done')], max_length=50, null=True),
        ),
    ]
