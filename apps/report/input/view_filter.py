from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import datetime
from django.conf import settings
from .forms import PengajuanForm,JvendorForm,PengajuanSatuForm,PengajuanDuaForm
from apps.products.models import Produk

@login_required(login_url=settings.LOGIN_URL)
def filter_pengajuan(request):
    user = request.user
    if request.method == 'POST':
        form = JvendorForm(request.POST)
        if form.is_valid():
            vendor = form.cleaned_data['jvendor']
            if vendor == '1':
                return redirect('/report/in_pengajuan_satu/%s/' %(vendor))
            elif vendor == '2':
                return redirect('in-pengajuan-dua')
            else:
                return redirect('in-pengajuan')
    else:
        form = JvendorForm()
    return render(request,'pengajuan/filter_pengajuan.html',{'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def input_pengajuan(request):
    sekarang = datetime.date.today()
    form = PengajuanForm(initial={'tanggal':sekarang})
    return render(request, 'pengajuan/pengajuan.html',{'forms':form})


@login_required(login_url=settings.LOGIN_URL)
def input_pengajuan_satu(request,jv):
    sekarang = datetime.date.today()
    form = PengajuanSatuForm(initial={'tanggal':sekarang,'jenis_produk':jv})
    return render(request, 'pengajuan/pengajuan_satu.html',{'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def input_pengajuan_dua(request):
    sekarang = datetime.date.today()
    form = PengajuanDuaForm(initial={'tanggal':sekarang})
    return render(request, 'pengajuan/pengajuan_dua.html',{'forms':form})