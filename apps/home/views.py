from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import datetime

from apps.products import models as pm 

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    sekarang = datetime.date.today()
    awal = datetime.date(sekarang.year,1,1)
    negara = pm.Negara.objects.filter(status=1).count()
    vendor = pm.JasaPengiriman.objects.filter(status=1).count()
    produk = pm.Produk.objects.filter(status=1).count()
    kurs = pm.Kurs.objects.filter(status_kurs=1).count()
    mata_uang = pm.MataUang.objects.filter(status=1).count()
    pr_job = pm.ParameterData.objects.filter(status_param=1).count()
    
    transaksi = pm.Transaksi.objects.filter(tanggal__range=(awal,sekarang)).count()
    on_proses = pm.Job.objects.filter(status_job__isnull = True).count()
    j_done = pm.Job.objects.filter(status_job = 1).count()
    total_invoice = on_proses + j_done
    return render(request,'home/index.html',{'ng':negara,'vd':vendor,'pr':produk,'tr':transaksi,
        'j_done':j_done,'on_proses':on_proses,'invoice':total_invoice,'kurs':kurs,'mt':mata_uang,
        'pr':pr_job})
    



