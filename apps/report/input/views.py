from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from apps.products.models import ParameterData, ParameterDataBl
from .forms import PengajuanForm

##### GAsti Asih = 10 ,LintasNegara = 18, dili= 5 ,antarlapan =19
@login_required(login_url=settings.LOGIN_URL)
def proses_input(request,param):
    param = ParameterData.objects.get(id = param)
    #print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,'ssssssss') 
    if param.products.origin_vendor.id == 1 and param.products.through_vendor.id == 3 and param.products.destinations_vendor.id ==5:
        return redirect('/report/save_input_satu/%s/'%(param)) ###ada Di direktori pecah View_satu.py       
    elif param.products.origin_vendor.id == 10 and param.products.through_vendor.id == 18 and param.products.destinations_vendor.id ==5:
        return redirect('/report/save_input_dua/%s/'%(param)) ###ada Di direktori pecah  View_satu.py   
    elif param.products.origin_vendor.id == 10 and param.products.through_vendor.id == 19 and param.products.destinations_vendor.id ==5:
        return redirect('/report/save_input_tiga/%s/'%(param)) ###ada Di direktori pecah View_satu.py   
    else:
        messages.success(request, 'Data Parameter Inputan Belum Ada, Hubungi IT ') 
        redirect('in-pengajuan')
    
    return redirect('in-pengajuan')    

@login_required(login_url=settings.LOGIN_URL)
def input_pengajuan(request):
    sekarang = datetime.date.today()
    form = PengajuanForm(initial={'tanggal':sekarang})
    return render(request, 'pengajuan/pengajuan.html',{'forms':form})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_simulasi_form(request, h_ajax, template_name):
    data = dict()
    context = {'h_ajax': h_ajax}
    data['django_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def showparam(request):
    jenis_produk = request.GET.get('jenis_produk',None)
    produk = request.GET.get('produk',None)
    tanggal = request.GET.get('tanggal',None)
    poin_satu = request.GET.get('poin_satu',None)
    poin_dua = request.GET.get('poin_dua',None)
    poin_tiga = request.GET.get('poin_tiga',None)
    origin_vendor = request.GET.get('origin_vendor',None)
    through_vendor = request.GET.get('through_vendor',None)
    destinations_vendor = request.GET.get('destinations_vendor',None)    
    
    param = ParameterData.objects.get(products=produk,products__point_satu=poin_satu,products__point_dua=poin_dua,
        products__point_tiga=poin_tiga,products__origin_vendor=origin_vendor,products__through_vendor=through_vendor,
        products__destinations_vendor=destinations_vendor,products__status=1,products__jenis_produk=jenis_produk)
    prd = param.products.kode_produk
    org_ven = param.products.origin_vendor
    org = param.products.point_satu
    h_ajax ={'tanggal':tanggal,'produk':prd,'param':param.id,'org':org,'org_ven':org_ven,'ds_ven':param.products.through_vendor,
        'ds': param.products.point_dua,'lt_ven':param.products.destinations_vendor,'lt':param.products.point_tiga,
        'js':param.products.jenis_produk,'jmlv':param.products.jumlah_vendor,}
    return save_simulasi_form(request, h_ajax,'pengajuan/addpengajuan.html')
    