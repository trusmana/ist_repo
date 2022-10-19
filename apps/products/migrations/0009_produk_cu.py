# Generated by Django 4.0.2 on 2022-09-29 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_alter_kurs_status_kurs_alter_matauang_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='cu',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cu_produk', to=settings.AUTH_USER_MODEL),
        ),
    ]
