# Generated by Django 4.0.2 on 2022-10-31 18:43

import apps.keuangan.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keuangan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nobukti', models.CharField(blank=True, default=apps.keuangan.models.number, max_length=350, null=True)),
                ('kre_jurnal', models.IntegerField(blank=True, null=True)),
                ('keterangan_transaksi', models.CharField(blank=True, max_length=500, null=True)),
                ('id_transaksi', models.CharField(blank=True, max_length=500, null=True)),
                ('object_id', models.IntegerField(blank=True, null=True)),
                ('diskripsi', models.CharField(blank=True, max_length=200, null=True)),
                ('kode_cabang', models.CharField(blank=True, max_length=5, null=True)),
                ('tgl_trans', models.DateField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
                ('cu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jurnal_creator', to=settings.AUTH_USER_MODEL)),
                ('mu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jurnal_modifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'jurnal',
            },
        ),
        migrations.CreateModel(
            name='Tbl_Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_trans', models.IntegerField(blank=True, null=True)),
                ('jenis', models.CharField(max_length=100)),
                ('debet', models.IntegerField()),
                ('kredit', models.IntegerField()),
                ('id_cabang', models.IntegerField()),
                ('status_jurnal', models.IntegerField()),
                ('status_reject', models.CharField(blank=True, choices=[('1', 'Reject'), ('3', 'Lanjut')], max_length=2, null=True)),
                ('tgl_trans', models.DateField()),
                ('status_posting', models.IntegerField(blank=True, null=True)),
                ('deskripsi', models.CharField(blank=True, max_length=500, null=True)),
                ('saldo', models.IntegerField(blank=True, null=True)),
                ('posting', models.CharField(blank=True, max_length=3, null=True)),
                ('jurnal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keuangan.jurnal')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_tbl_transaksi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_transaksi',
            },
        ),
    ]
