# Generated by Django 4.0.2 on 2022-09-16 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MataUang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'NonAktif'), ('1', 'Aktif')], max_length=10, null=True)),
                ('nama_mata_uang', models.CharField(blank=True, max_length=30, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('cu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_mt', to=settings.AUTH_USER_MODEL)),
                ('mu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mu_mt', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'MataUang',
            },
        ),
    ]
