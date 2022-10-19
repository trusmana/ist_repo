from unicodedata import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from apps.products.models import  ParameterDataBl
from decimal import Decimal

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def cartage_warehouse_charge_one(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        
        if int(dt)>int(1) and int(dt)<=int(pa.min_cartage_and_warehouse_charge):
            nilai = Decimal(dt) * Decimal(pa.price_cartage_and_warehouse_charge)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_cartage_and_warehouse_charge)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def cartage_warehouse_charge_two(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_cartage_and_warehouse_charge):
            nilai = Decimal(dt) * Decimal(pa.price_cartage_and_warehouse_charge)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_cartage_and_warehouse_charge)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def ground_handling_sale(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_ground_handling):
            nilai = Decimal(dt) * Decimal(pa.price_ground_handling)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_ground_handling)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def warehouse_charge_sale(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_warehouse_charge):
            nilai = Decimal(dt) * Decimal(pa.price_doc_and_clearance)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_warehouse_charge)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def handling_charge_sale(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_handling_charge):
            nilai = Decimal(dt) * Decimal(pa.price_handling_charge)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_handling_charge)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def delivery_sale(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_delivery):
            nilai = Decimal(dt) * Decimal(pa.price_delivery)
        else:
            nilai = Decimal(dt) * Decimal(pa.price_delivery)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def freight_sale(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        dt = request.GET.get('kali')
        pa = ParameterDataBl.objects.get(id= int(id_param))
        if Decimal(dt)> Decimal(1) and Decimal(dt)<=Decimal(pa.min_airfreight_sin_dps_dil):
            nilai = Decimal(dt) * Decimal(pa.airfreight_sin_dps_dil)
        else:
            nilai = Decimal(dt) * Decimal(pa.airfreight_sin_dps_dil)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))