# Generated by Django 4.0.2 on 2022-10-31 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiayaPusat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(help_text='Tahun-bl-tg', null=True)),
                ('saldo_awal', models.FloatField(default=0)),
                ('saldo_akhir', models.FloatField(blank=True, default=0, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=500, null=True)),
                ('jenis_keterangan', models.CharField(blank=True, max_length=6, null=True)),
                ('cu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_biaya', to=settings.AUTH_USER_MODEL)),
                ('ket_cabang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.cabang')),
                ('mu', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mu_biaya', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'BiayaPusat',
                'db_table': 'biayapusat',
                'ordering': ['-tanggal'],
            },
        ),
    ]
