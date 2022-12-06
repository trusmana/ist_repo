from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import redirect,render
from django.contrib import messages
from django.conf import settings
import datetime

from apps.report.parameter.paramdata import form as fm
from apps.products.models import ParameterData,Produk

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT','OPERASIONAL')))  # type: ignore
def addparam(request,pr,origin,through,destn):
    #### 1 = fs , 3 = so, 5 =dest
    user = request.user
    dt = Produk.objects.get(id=pr)
    print('or', origin,through,destn)
    ######Pramaeter FS SLDL
    if origin == 1 and through == 3 and destn == 5:
        if request.method == 'POST':
            form = fm.FSForm(request.POST)
            form2 = fm.SLForm(request.POST)
            form3 = fm.DLForm(request.POST)
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                saveform(dt,form,form2,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form = fm.FSForm()
            form2 = fm.SLForm()
            form3 = fm.DLForm()
        return render(request,'report/parameter/add_parameter3.html',{'forms':form,'forms2':form2,'forms3':form3,'dt':dt})
    ### iD Gasti Asih , DPS Solid Dili Lintas Negara    
    elif origin == 10 and through == 3 and destn == 5:
        if request.method == 'POST':
            form = fm.GastiAsihForm(request.POST)
            form2 = fm.SLForm(request.POST)
            form3 = fm.DLForm(request.POST)
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                saveform2(dt,form,form2,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form = fm.GastiAsihForm()
            form2 = fm.SLForm()
            form3 = fm.DLForm()
        return render(request,'report/parameter/add_parameter3.html',{'forms':form,'forms2':form2,'forms3':form3,'dt':dt})    
    else:
        messages.success(request, 'Data Parameter Belum Ada, Hubungi Administrator')
        return redirect('add-paramdta')

####Khusus GS SF DL
def saveform2(dt,form,form2,form3,user):
    min_pcs = form.cleaned_data['min_pcs']
    price_pcs = form.cleaned_data['price_pcs']
    price_high_pcs = form.cleaned_data['price_high_pcs']

    min_weight = form.cleaned_data['min_weight']
    price_weight = form.cleaned_data['price_weight']
    price_high_weight = form.cleaned_data['price_high_weight']
    
    min_handling = form.cleaned_data['min_handling']
    price_handling = form.cleaned_data['price_handling']
    price_high_handling = form.cleaned_data['price_high_handling']
    
    min_transportation_charge = form.cleaned_data['min_transportation_charge']
    price_transportation_charge = form.cleaned_data['price_transportation_charge']
    price_high_transportation_charge = form.cleaned_data['price_high_transportation_charge']    
    
    ###sl
    price_high_storage_at_cost = form2.cleaned_data['price_high_storage_at_cost']
    min_storage_at_cost = form2.cleaned_data['min_storage_at_cost']
    price_storage_at_cost = form2.cleaned_data['price_storage_at_cost']

    min_pjkp2u_sin_dps_at_cost = form2.cleaned_data['min_pjkp2u_sin_dps_at_cost']
    price_high_pjkp2u_sin_dps_at_cost = form2.cleaned_data['price_high_pjkp2u_sin_dps_at_cost']
    price_pjkp2u_sin_dps_at_cost = form2.cleaned_data['price_pjkp2u_sin_dps_at_cost']

    min_storage_mcl_e_0389249_at_cost = form2.cleaned_data['min_storage_mcl_e_0389249_at_cost']
    price_high_storage_mcl_e_0389249_at_cost = form2.cleaned_data['price_high_storage_mcl_e_0389249_at_cost']
    price_storage_mcl_e_0389249_at_cost = form2.cleaned_data['price_storage_mcl_e_0389249_at_cost']

    min_pjkp2u_dps_dil_at_cost = form2.cleaned_data['min_pjkp2u_dps_dil_at_cost']
    price_high_pjkp2u_dps_dil_at_cost = form2.cleaned_data['price_high_pjkp2u_dps_dil_at_cost']
    price_pjkp2u_dps_dil_at_cost = form2.cleaned_data['price_pjkp2u_dps_dil_at_cost']
    ######### Biaya Storege
    min_airfreight_charges = form2.cleaned_data['min_airfreight_charges']
    price_high_airfreight_charges = form2.cleaned_data['price_high_airfreight_charges']
    price_airfreight_charges = form2.cleaned_data['price_airfreight_charges']

    price_high_overweight_charges_surcharge = form2.cleaned_data['price_high_overweight_charges_surcharge']
    min_overweight_charges_surcharge = form2.cleaned_data['min_overweight_charges_surcharge']
    price_overweight_charges_surcharge = form2.cleaned_data['price_overweight_charges_surcharge']

    price_high_awb_fee = form2.cleaned_data['price_high_awb_fee']
    min_awb_fee = form2.cleaned_data['min_awb_fee']
    price_awb_fee = form2.cleaned_data['price_awb_fee']

    price_high_handling_charges_sl = form2.cleaned_data['price_high_handling_charges_sl']
    min_handling_charges_sl = form2.cleaned_data['min_handling_charges_sl']
    price_handling_charges_sl = form2.cleaned_data['price_handling_charges_sl']
    ###sl
    
    ### dl 
    
    min_ground_handling_dl = form3.cleaned_data['min_ground_handling_dl']
    price_ground_handling_dl = form3.cleaned_data['price_ground_handling_dl']
    price_high_ground_handling_dl = form3.cleaned_data['price_high_ground_handling_dl']
    
    min_forklift_for_heavy_cargo = form3.cleaned_data['min_forklift_for_heavy_cargo']
    price_forklift_for_heavy_cargo = form3.cleaned_data['price_forklift_for_heavy_cargo']
    price_high_forklift_for_heavy_cargo = form3.cleaned_data['price_high_forklift_for_heavy_cargo']
    
    min_custom_clearance = form3.cleaned_data['min_custom_clearance']
    price_custom_clearance = form3.cleaned_data['price_custom_clearance']
    price_high_custom_clearance = form3.cleaned_data['price_high_custom_clearance']
    
    min_delivey_to_hera = form3.cleaned_data['min_delivey_to_hera']
    price_delivey_to_hera = form3.cleaned_data['price_delivey_to_hera']
    price_high_delivey_to_hera = form3.cleaned_data['price_high_delivey_to_hera']
    
    min_akses_bandara_inspeksi = form3.cleaned_data['min_akses_bandara_inspeksi']
    price_akses_bandara_inspeksi = form3.cleaned_data['price_akses_bandara_inspeksi']
    price_high_akses_bandara_inspeksi = form3.cleaned_data['price_high_akses_bandara_inspeksi']
    
    min_handling_fee = form3.cleaned_data['min_handling_fee']
    price_handling_fee = form3.cleaned_data['price_handling_fee']
    price_high_handling_fee = form3.cleaned_data['price_high_handling_fee']
    
    min_admin_fee = form3.cleaned_data['min_admin_fee']
    admin_fee = form3.cleaned_data['admin_fee']
    admin_high_fee = form3.cleaned_data['admin_high_fee']
    
    min_fee_collection = form3.cleaned_data['min_fee_collection']
    fee_collection = form3.cleaned_data['fee_collection']
    fee_high_collection = form3.cleaned_data['fee_high_collection']    
    ### dl 
    
    prm = ParameterData(products = dt,j_vendor=3,status_param = 1,tgl_aktif_param= datetime.date.today(),cu=user,
        min_pcs = min_pcs,price_pcs = price_pcs,price_high_pcs = price_high_pcs,
        min_weight = min_weight,price_weight = price_weight,price_high_weight = price_high_weight,

        min_handling = min_handling,price_handling = price_handling,price_high_handling = price_high_handling,
        
        min_transportation_charge = min_transportation_charge,
        price_transportation_charge = price_transportation_charge,
        price_high_transportation_charge = price_high_transportation_charge,
        ###sl
        price_high_storage_at_cost =price_high_storage_at_cost,min_storage_at_cost =min_storage_at_cost,
        price_storage_at_cost =price_storage_at_cost,
        min_pjkp2u_sin_dps_at_cost = min_pjkp2u_sin_dps_at_cost,
        price_high_pjkp2u_sin_dps_at_cost =price_high_pjkp2u_sin_dps_at_cost,
        price_pjkp2u_sin_dps_at_cost =price_pjkp2u_sin_dps_at_cost,
        min_storage_mcl_e_0389249_at_cost =min_storage_mcl_e_0389249_at_cost,
        price_high_storage_mcl_e_0389249_at_cost =price_high_storage_mcl_e_0389249_at_cost,
        price_storage_mcl_e_0389249_at_cost =price_storage_mcl_e_0389249_at_cost,
        min_pjkp2u_dps_dil_at_cost =min_pjkp2u_dps_dil_at_cost,
        price_high_pjkp2u_dps_dil_at_cost =price_high_pjkp2u_dps_dil_at_cost,
        price_pjkp2u_dps_dil_at_cost =price_pjkp2u_dps_dil_at_cost,min_airfreight_charges =min_airfreight_charges,
        price_high_airfreight_charges =price_high_airfreight_charges,
        price_airfreight_charges =price_airfreight_charges,
        price_high_overweight_charges_surcharge =price_high_overweight_charges_surcharge,
        min_overweight_charges_surcharge =min_overweight_charges_surcharge,price_overweight_charges_surcharge =price_overweight_charges_surcharge,
        price_high_awb_fee =price_high_awb_fee,min_awb_fee =min_awb_fee,price_awb_fee =price_awb_fee, 
        price_high_handling_charges_sl =price_high_handling_charges_sl,min_handling_charges_sl =min_handling_charges_sl,
        price_handling_charges_sl =price_handling_charges_sl,
        ##dl
        min_ground_handling_dl = min_ground_handling_dl,price_ground_handling_dl = price_ground_handling_dl,
        price_high_ground_handling_dl = price_high_ground_handling_dl,min_forklift_for_heavy_cargo = min_forklift_for_heavy_cargo,
        price_forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
        price_high_forklift_for_heavy_cargo = price_high_forklift_for_heavy_cargo,
        min_custom_clearance = min_custom_clearance,price_custom_clearance = price_custom_clearance,
        price_high_custom_clearance = price_high_custom_clearance,min_delivey_to_hera = min_delivey_to_hera,
        price_delivey_to_hera = price_delivey_to_hera,price_high_delivey_to_hera = price_high_delivey_to_hera,
        min_akses_bandara_inspeksi = min_akses_bandara_inspeksi,price_akses_bandara_inspeksi = price_akses_bandara_inspeksi,
        price_high_akses_bandara_inspeksi = price_high_akses_bandara_inspeksi,
        min_handling_fee = min_handling_fee,price_handling_fee = price_handling_fee,price_high_handling_fee = price_high_handling_fee,
        min_admin_fee = min_admin_fee,admin_fee = admin_fee,admin_high_fee = admin_high_fee,min_fee_collection = min_fee_collection,
        fee_collection = fee_collection,fee_high_collection = fee_high_collection,
        )
    prm.save()    


####Khusus FS SF DL
def saveform(dt,form,form2,form3,user):
    min_airfreight = form.cleaned_data['min_airfreight']
    price_min_airfreight = form.cleaned_data['price_min_airfreight']
    price_max_airfreight = form.cleaned_data['price_max_airfreight']
    price_max_handling_charges = form.cleaned_data['price_max_handling_charges']
    min_handling_charges = form.cleaned_data['min_handling_charges']
    price_min_handling_charges = form.cleaned_data['price_min_handling_charges']
    
    min_insurance_security_surcharge = form.cleaned_data['min_insurance_security_surcharge']
    price_insurance_security_surcharge = form.cleaned_data['price_insurance_security_surcharge']
    price_high_insurance_security_surcharge = form.cleaned_data['price_high_insurance_security_surcharge']
    
    min_fuel_surcharge = form.cleaned_data['min_fuel_surcharge']
    price_fuel_surcharge = form.cleaned_data['price_fuel_surcharge']
    price_high_fuel_surcharge = form.cleaned_data['price_high_fuel_surcharge']
    
    min_import_handling_charges = form.cleaned_data['min_import_handling_charges']
    price_import_handling_charges = form.cleaned_data['price_import_handling_charges']
    price_high_import_handling_charges = form.cleaned_data['price_high_import_handling_charges']
    
    
    min_gst_zero_rated = form.cleaned_data['min_gst_zero_rated']
    price_gst_zero_rated = form.cleaned_data['price_gst_zero_rated']
    price_high_gst_zero_rated = form.cleaned_data['price_high_gst_zero_rated']
    
    ###sl
    price_high_storage_at_cost = form2.cleaned_data['price_high_storage_at_cost']
    min_storage_at_cost = form2.cleaned_data['min_storage_at_cost']
    price_storage_at_cost = form2.cleaned_data['price_storage_at_cost']

    min_pjkp2u_sin_dps_at_cost = form2.cleaned_data['min_pjkp2u_sin_dps_at_cost']
    price_high_pjkp2u_sin_dps_at_cost = form2.cleaned_data['price_high_pjkp2u_sin_dps_at_cost']
    price_pjkp2u_sin_dps_at_cost = form2.cleaned_data['price_pjkp2u_sin_dps_at_cost']

    min_storage_mcl_e_0389249_at_cost = form2.cleaned_data['min_storage_mcl_e_0389249_at_cost']
    price_high_storage_mcl_e_0389249_at_cost = form2.cleaned_data['price_high_storage_mcl_e_0389249_at_cost']
    price_storage_mcl_e_0389249_at_cost = form2.cleaned_data['price_storage_mcl_e_0389249_at_cost']

    min_pjkp2u_dps_dil_at_cost = form2.cleaned_data['min_pjkp2u_dps_dil_at_cost']
    price_high_pjkp2u_dps_dil_at_cost = form2.cleaned_data['price_high_pjkp2u_dps_dil_at_cost']
    price_pjkp2u_dps_dil_at_cost = form2.cleaned_data['price_pjkp2u_dps_dil_at_cost']
    ######### Biaya Storege
    min_airfreight_charges = form2.cleaned_data['min_airfreight_charges']
    price_high_airfreight_charges = form2.cleaned_data['price_high_airfreight_charges']
    price_airfreight_charges = form2.cleaned_data['price_airfreight_charges']

    price_high_overweight_charges_surcharge = form2.cleaned_data['price_high_overweight_charges_surcharge']
    min_overweight_charges_surcharge = form2.cleaned_data['min_overweight_charges_surcharge']
    price_overweight_charges_surcharge = form2.cleaned_data['price_overweight_charges_surcharge']

    price_high_awb_fee = form2.cleaned_data['price_high_awb_fee']
    min_awb_fee = form2.cleaned_data['min_awb_fee']
    price_awb_fee = form2.cleaned_data['price_awb_fee']

    price_high_handling_charges_sl = form2.cleaned_data['price_high_handling_charges_sl']
    min_handling_charges_sl = form2.cleaned_data['min_handling_charges_sl']
    price_handling_charges_sl = form2.cleaned_data['price_handling_charges_sl']
    ###sl
    
    ### dl 
    
    min_ground_handling_dl = form3.cleaned_data['min_ground_handling_dl']
    price_ground_handling_dl = form3.cleaned_data['price_ground_handling_dl']
    price_high_ground_handling_dl = form3.cleaned_data['price_high_ground_handling_dl']
    
    min_forklift_for_heavy_cargo = form3.cleaned_data['min_forklift_for_heavy_cargo']
    price_forklift_for_heavy_cargo = form3.cleaned_data['price_forklift_for_heavy_cargo']
    price_high_forklift_for_heavy_cargo = form3.cleaned_data['price_high_forklift_for_heavy_cargo']
    
    min_custom_clearance = form3.cleaned_data['min_custom_clearance']
    price_custom_clearance = form3.cleaned_data['price_custom_clearance']
    price_high_custom_clearance = form3.cleaned_data['price_high_custom_clearance']
    
    min_delivey_to_hera = form3.cleaned_data['min_delivey_to_hera']
    price_delivey_to_hera = form3.cleaned_data['price_delivey_to_hera']
    price_high_delivey_to_hera = form3.cleaned_data['price_high_delivey_to_hera']
    
    min_akses_bandara_inspeksi = form3.cleaned_data['min_akses_bandara_inspeksi']
    price_akses_bandara_inspeksi = form3.cleaned_data['price_akses_bandara_inspeksi']
    price_high_akses_bandara_inspeksi = form3.cleaned_data['price_high_akses_bandara_inspeksi']
    
    min_handling_fee = form3.cleaned_data['min_handling_fee']
    price_handling_fee = form3.cleaned_data['price_handling_fee']
    price_high_handling_fee = form3.cleaned_data['price_high_handling_fee']
    
    min_admin_fee = form3.cleaned_data['min_admin_fee']
    admin_fee = form3.cleaned_data['admin_fee']
    admin_high_fee = form3.cleaned_data['admin_high_fee']
    
    min_fee_collection = form3.cleaned_data['min_fee_collection']
    fee_collection = form3.cleaned_data['fee_collection']
    fee_high_collection = form3.cleaned_data['fee_high_collection']
    
    ### dl 
    
    prm = ParameterData(products = dt,j_vendor=3,status_param = 1,tgl_aktif_param= datetime.date.today(),cu=user,
        min_airfreight = min_airfreight,price_min_airfreight = price_min_airfreight,price_max_airfreight = price_max_airfreight,
        price_max_handling_charges = price_max_handling_charges,min_handling_charges = min_handling_charges,
        price_min_handling_charges = price_min_handling_charges,
        min_insurance_security_surcharge = min_insurance_security_surcharge,
        price_insurance_security_surcharge = price_insurance_security_surcharge,
        price_high_insurance_security_surcharge = price_high_insurance_security_surcharge,
        price_high_fuel_surcharge = price_high_fuel_surcharge,min_fuel_surcharge = min_fuel_surcharge,
        price_fuel_surcharge = price_fuel_surcharge,price_high_import_handling_charges = price_high_import_handling_charges,
        min_import_handling_charges = min_import_handling_charges,price_import_handling_charges = price_import_handling_charges,
        price_high_gst_zero_rated = price_high_gst_zero_rated,min_gst_zero_rated = min_gst_zero_rated,
        price_gst_zero_rated = price_gst_zero_rated,###sl
        price_high_storage_at_cost =price_high_storage_at_cost,min_storage_at_cost =min_storage_at_cost,
        price_storage_at_cost =price_storage_at_cost,
        min_pjkp2u_sin_dps_at_cost = min_pjkp2u_sin_dps_at_cost,
        price_high_pjkp2u_sin_dps_at_cost =price_high_pjkp2u_sin_dps_at_cost,
        price_pjkp2u_sin_dps_at_cost =price_pjkp2u_sin_dps_at_cost,
        min_storage_mcl_e_0389249_at_cost =min_storage_mcl_e_0389249_at_cost,
        price_high_storage_mcl_e_0389249_at_cost =price_high_storage_mcl_e_0389249_at_cost,
        price_storage_mcl_e_0389249_at_cost =price_storage_mcl_e_0389249_at_cost,
        min_pjkp2u_dps_dil_at_cost =min_pjkp2u_dps_dil_at_cost,
        price_high_pjkp2u_dps_dil_at_cost =price_high_pjkp2u_dps_dil_at_cost,
        price_pjkp2u_dps_dil_at_cost =price_pjkp2u_dps_dil_at_cost,min_airfreight_charges =min_airfreight_charges,
        price_high_airfreight_charges =price_high_airfreight_charges,
        price_airfreight_charges =price_airfreight_charges,
        price_high_overweight_charges_surcharge =price_high_overweight_charges_surcharge,
        min_overweight_charges_surcharge =min_overweight_charges_surcharge,price_overweight_charges_surcharge =price_overweight_charges_surcharge,
        price_high_awb_fee =price_high_awb_fee,min_awb_fee =min_awb_fee,price_awb_fee =price_awb_fee, 
        price_high_handling_charges_sl =price_high_handling_charges_sl,min_handling_charges_sl =min_handling_charges_sl,
        price_handling_charges_sl =price_handling_charges_sl,##dl
        min_ground_handling_dl = min_ground_handling_dl,price_ground_handling_dl = price_ground_handling_dl,
        price_high_ground_handling_dl = price_high_ground_handling_dl,min_forklift_for_heavy_cargo = min_forklift_for_heavy_cargo,
        price_forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
        price_high_forklift_for_heavy_cargo = price_high_forklift_for_heavy_cargo,
        min_custom_clearance = min_custom_clearance,price_custom_clearance = price_custom_clearance,
        price_high_custom_clearance = price_high_custom_clearance,min_delivey_to_hera = min_delivey_to_hera,
        price_delivey_to_hera = price_delivey_to_hera,price_high_delivey_to_hera = price_high_delivey_to_hera,
        min_akses_bandara_inspeksi = min_akses_bandara_inspeksi,price_akses_bandara_inspeksi = price_akses_bandara_inspeksi,
        price_high_akses_bandara_inspeksi = price_high_akses_bandara_inspeksi,
        min_handling_fee = min_handling_fee,price_handling_fee = price_handling_fee,price_high_handling_fee = price_high_handling_fee,
        min_admin_fee = min_admin_fee,admin_fee = admin_fee,admin_high_fee = admin_high_fee,min_fee_collection = min_fee_collection,
        fee_collection = fee_collection,fee_high_collection = fee_high_collection,
        )
    prm.save()

