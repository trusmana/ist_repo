# Generated by Django 4.0.2 on 2022-09-28 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_matauang_negara'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_kurs', models.CharField(choices=[('0', 'NonAktif'), ('1', 'Aktif')], max_length=10)),
                ('nilai_kurs', models.FloatField(blank=True, null=True)),
                ('tanggal_aktif', models.DateField(blank=True, null=True)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('cu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_kurs', to=settings.AUTH_USER_MODEL)),
                ('mtu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtu_fk', to='products.matauang')),
                ('mu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mu_kurs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kurs',
            },
        ),
    ]
