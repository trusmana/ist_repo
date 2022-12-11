from unicodedata import decimal
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from apps.products.models import ParameterData
from decimal import Decimal

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def airfreight(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        airfreight = request.GET.get('airfreight')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(airfreight)>Decimal(1) and Decimal(airfreight)<=Decimal(pa.min_airfreight) :  # type: ignore
            nilai = Decimal(airfreight) * Decimal(pa.price_min_airfreight)  # type: ignore
        else:
            nilai = Decimal(airfreight) * Decimal(pa.price_max_airfreight)  # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def handling_charges(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        handling = request.GET.get('handling')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(handling) > Decimal(1) and Decimal(handling) <= Decimal(pa.min_handling_charges) :  # type: ignore
            nilai = Decimal(pa.price_min_handling_charges) * Decimal(handling)           # type: ignore
        else:
            nilai = Decimal(pa.price_max_handling_charges) * Decimal(handling)   # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def insurance_security(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        asuransi = request.GET.get('asuransi')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(asuransi) > Decimal(1) and Decimal(asuransi) <= Decimal(pa.min_insurance_security_surcharge) :  # type: ignore
            nilai = Decimal(asuransi) * Decimal(pa.price_insurance_security_surcharge)          # type: ignore
        else:
            nilai = Decimal(asuransi) * Decimal(pa.price_high_insurance_security_surcharge)  # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def fuel_surcharge(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        bahanbakar = request.GET.get('bahanbakar')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(bahanbakar) > Decimal(1) and Decimal(bahanbakar) <= Decimal(pa.min_fuel_surcharge) :  # type: ignore
            nilai = Decimal(bahanbakar) * Decimal(pa.price_fuel_surcharge)          # type: ignore
        else:
            nilai = Decimal(bahanbakar) * Decimal(pa.price_high_fuel_surcharge)  # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def import_handling_charges(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        penanganan = request.GET.get('penanganan')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(penanganan) > Decimal(1) and Decimal(penanganan) <= Decimal(pa.min_import_handling_charges) :  # type: ignore
            nilai = Decimal(penanganan) * int(pa.price_import_handling_charges)          # type: ignore
        else:
            nilai = Decimal(penanganan) * Decimal(pa.price_high_import_handling_charges)  # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def gst_zero_rated(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        zero = request.GET.get('zero')
        pa = ParameterData.objects.get(id= Decimal(id_param))
        if Decimal(zero) > Decimal(1) and Decimal(zero) <= Decimal(pa.min_gst_zero_rated) :  # type: ignore
            nilai = Decimal(zero) * Decimal(pa.price_gst_zero_rated)        # type: ignore
        else:
            nilai = Decimal(zero) * Decimal(pa.price_high_gst_zero_rated) # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))


#####Ajax Form 2 Sholid Logistik
def currency_storage_at_cost(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_storage_at_cost) :  # type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_storage_at_cost)   # type: ignore     
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_storage_at_cost)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def pjkp2u_sin_dps_at_cost(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_pjkp2u_sin_dps_at_cost) :# type: ignore
            nilai = int(tmp) * int(pa.price_pjkp2u_sin_dps_at_cost ) # type: ignore       
        else:
            nilai = int(tmp) * int(pa.price_high_pjkp2u_sin_dps_at_cost) # type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def storage_mcl_e_0389249_at_cost(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_storage_at_cost) :# type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_storage_at_cost )           # type: ignore 
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_storage_at_cost)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def pjkp2u_dps_dil_at_cost(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_pjkp2u_dps_dil_at_cost) : # type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_pjkp2u_dps_dil_at_cost) # type: ignore           
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_pjkp2u_dps_dil_at_cost)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def airfreight_charges(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_airfreight_charges) :# type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_airfreight_charges)            # type: ignore
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_airfreight_charges)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_overweight_charges_surcharge(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_overweight_charges_surcharge) :# type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_overweight_charges_surcharge)            # type: ignore
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_overweight_charges_surcharge)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def cek_currency_awb_fee(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_awb_fee) :# type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_awb_fee)            # type: ignore
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_awb_fee)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_handling_charges(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_handling_charges_sl) :# type: ignore
            nilai = Decimal(tmp) * Decimal(pa.price_handling_charges_sl)            # type: ignore
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_handling_charges_sl)# type: ignore
        data = {'result':'1','param':id_param,'price':nilai}            # type: ignore
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))
#####End Sholidlogistik

##########logistik DILI
def currency_ground_handling(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_ground_handling_dl) :
            nilai = Decimal(tmp) * Decimal(pa.price_ground_handling_dl)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_ground_handling_dl)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_forklift_for_heavy_cargo(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_forklift_for_heavy_cargo) :
            nilai = Decimal(tmp) * Decimal(pa.price_forklift_for_heavy_cargo)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_forklift_for_heavy_cargo)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_custom_clearance(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_custom_clearance) :
            nilai = Decimal(tmp) * Decimal(pa.price_custom_clearance)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_custom_clearance)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_delivey_to_hera(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= Decimal(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_delivey_to_hera) :
            nilai = Decimal(tmp) * Decimal(pa.price_delivey_to_hera)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_delivey_to_hera)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_akses_bandara_inspeksi(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= Decimal(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_akses_bandara_inspeksi) :
            nilai = Decimal(tmp) * Decimal(pa.price_akses_bandara_inspeksi)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_akses_bandara_inspeksi)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_handling_fee(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= int(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_handling_fee) :
            nilai = Decimal(tmp) * Decimal(pa.price_handling_fee)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.price_high_handling_fee)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_admin_fee(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= Decimal(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_admin_fee) :
            nilai = Decimal(tmp) * Decimal(pa.admin_fee)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.admin_high_fee)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))

def currency_fee_collection(request):
    data = {'result':0,'param':0,'price':0}
    if is_ajax(request=request):
        id_param = request.GET.get('prm')
        tmp = request.GET.get('tmp')
        pa = ParameterData.objects.get(id= Decimal(id_param))        
        if Decimal(tmp) > Decimal(1) and Decimal(tmp) <= Decimal(pa.min_fee_collection) :
            nilai = Decimal(tmp) * Decimal(pa.fee_collection)            
        else:
            nilai = Decimal(tmp) * Decimal(pa.fee_high_collection)
        data = {'result':'1','param':id_param,'price':nilai}            
        return HttpResponse(JsonResponse(data))
    else:
        return HttpResponse(JsonResponse(data))