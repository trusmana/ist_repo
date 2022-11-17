from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponse,JsonResponse
from apps.products import models as m_po
from apps.paramvendor import models as prm_v

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

#### Origin Khusus Yg Posisi Vendornya di origin
def gastiasih_origin(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        pcs = request.GET.get('pcs')
        weight = request.GET.get('weight')
        jenis = request.GET.get('jenis')
        paking = request.GET.get('paking')
        
        pa = m_po.ParameterData.objects.get(id=(id_param))
        if prm_v.GastiAsih.objects.get(jenis_angkutan=jenis):
            vv = prm_v.GastiAsih.objects.get(jenis_angkutan=jenis)
            print(type(weight),'ttttttttttttttt')
            nilai = (( (Decimal(weight)) * Decimal(vv.rate))) + Decimal(paking)
            data = {'result':'1','param':id_param,'price':nilai}
            return HttpResponse(JsonResponse(data))
        else:
            data = {'result':0,'param':0,'price':0}
            return HttpResponse(JsonResponse(data))        
        
    else:
        return HttpResponse(JsonResponse(data))
