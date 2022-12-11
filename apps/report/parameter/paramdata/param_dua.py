from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import redirect,render
from django.contrib import messages
from django.conf import settings
import datetime

from apps.report.parameter.paramdata import form as fm
from apps.products.models import ParameterData,Produk

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT','OPERASIONAL')))  # type: ignore
def addparamdua(request,pr,origin,destn):
    #### 1 = fs , 3 = so, 5 =dest
    user = request.user
    dt = Produk.objects.get(id=pr)
    print('or', origin,destn)
    ######Pramaeter FS DL
    if origin == 1 and destn == 5:
        if request.method == 'POST':
            form = fm.FSForm(request.POST)
            form3 = fm.DLForm(request.POST)
            if form.is_valid() and form3.is_valid():
                saveform(dt,form,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form = fm.FSForm()
            form3 = fm.DLForm()
        return render(request,'report/parameter/add/add_parameter2.html',{'forms':form,'forms3':form3,'dt':dt})
    if origin == 5 and destn == 1:
        print('cccccccccccccc')
        if request.method == 'POST':
            form3 = fm.DLForm(request.POST)
            form = fm.FSForm(request.POST)
            if form.is_valid() and form3.is_valid():
                saveform(dt,form,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form3 = fm.DLForm()
            form = fm.FSForm()
        return render(request,'report/parameter/add/add_parameter2.html',{'forms':form,'forms3':form3,'dt':dt})
    ## Sing DIL , DHL DIL
    if origin == 8 and destn == 5:
        if request.method == 'POST':
            form = fm.DHLForm(request.POST)
            form3 = fm.DLForm(request.POST)
            if form.is_valid() and form3.is_valid():
                savesatuform(dt,form,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form = fm.DHLForm()
            form3 = fm.DLForm()
        return render(request,'report/parameter/add/add_parameter2.html',{'forms':form,'forms3':form3,'dt':dt}) 
    ## DIL Sing , DHL Fs
    if origin == 8 and destn == 1:
        if request.method == 'POST':
            form = fm.DHLForm(request.POST)
            form3 = fm.FSForm(request.POST)
            if form.is_valid() and form3.is_valid():
                saveduaform(dt,form,form3,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-param')
        else:
            form = fm.DHLForm()
            form3 = fm.FSForm()
        return render(request,'report/parameter/add/add_parameter2.html',{'forms':form,'forms3':form3,'dt':dt})     
    else:
        messages.success(request, 'Data Parameter Belum Ada, Hubungi Administrator')
        return redirect('add-paramdta')

####Khusus FS  DL
def saveform(dt,form,form3,user):
    ## FS
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
    
    prm = ParameterData(products = dt,j_vendor =2,status_param = 1,tgl_aktif_param= datetime.date.today(),cu=user,
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
        price_gst_zero_rated = price_gst_zero_rated,
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

#### DHL DILI    
def savesatuform(dt,form,form3,user):
    ### DHL 
    min_express_wordwide_nondoc = form.cleaned_data['min_express_wordwide_nondoc']
    price_express_wordwide_nondoc = form.cleaned_data['price_express_wordwide_nondoc']
    price_high_express_wordwide_nondoc = form.cleaned_data['price_high_express_wordwide_nondoc']
    
    min_fuel_surcharge_dhl = form.cleaned_data['min_fuel_surcharge_dhl']
    price_fuel_surcharge_dhl = form.cleaned_data['price_fuel_surcharge_dhl']
    price_high_fuel_surcharge_dhl = form.cleaned_data['price_high_fuel_surcharge_dhl']

    min_emergency_situation = form.cleaned_data['min_emergency_situation']
    price_emergency_situation = form.cleaned_data['price_emergency_situation']
    price_high_emergency_situation = form.cleaned_data['price_high_emergency_situation']
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
    
    prm = ParameterData(products = dt,j_vendor =2,status_param = 1,tgl_aktif_param= datetime.date.today(),cu=user,
        min_express_wordwide_nondoc =min_express_wordwide_nondoc,price_express_wordwide_nondoc =price_express_wordwide_nondoc,
        price_high_express_wordwide_nondoc =price_high_express_wordwide_nondoc,
        min_fuel_surcharge_dhl = min_fuel_surcharge_dhl,
        price_fuel_surcharge_dhl = price_fuel_surcharge_dhl,
        price_high_fuel_surcharge_dhl = price_high_fuel_surcharge_dhl,
        min_emergency_situation = min_emergency_situation,
        price_emergency_situation = price_emergency_situation,
        price_high_emergency_situation = price_high_emergency_situation,
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

#### DHL DILI    
def saveduaform(dt,form,form3,user):
    ### DHL 
    min_express_wordwide_nondoc = form.cleaned_data['min_express_wordwide_nondoc']
    price_express_wordwide_nondoc = form.cleaned_data['price_express_wordwide_nondoc']
    price_high_express_wordwide_nondoc = form.cleaned_data['price_high_express_wordwide_nondoc']
    
    min_fuel_surcharge_dhl = form.cleaned_data['min_fuel_surcharge_dhl']
    price_fuel_surcharge_dhl = form.cleaned_data['price_fuel_surcharge_dhl']
    price_high_fuel_surcharge_dhl = form.cleaned_data['price_high_fuel_surcharge_dhl']

    min_emergency_situation = form.cleaned_data['min_emergency_situation']
    price_emergency_situation = form.cleaned_data['price_emergency_situation']
    price_high_emergency_situation = form.cleaned_data['price_high_emergency_situation']
    ### fs 
    min_airfreight = form3.cleaned_data['min_airfreight']
    price_min_airfreight = form3.cleaned_data['price_min_airfreight']
    price_max_airfreight = form3.cleaned_data['price_max_airfreight']
    price_max_handling_charges = form3.cleaned_data['price_max_handling_charges']
    min_handling_charges = form3.cleaned_data['min_handling_charges']
    price_min_handling_charges = form3.cleaned_data['price_min_handling_charges']
    
    min_insurance_security_surcharge = form3.cleaned_data['min_insurance_security_surcharge']
    price_insurance_security_surcharge = form3.cleaned_data['price_insurance_security_surcharge']
    price_high_insurance_security_surcharge = form3.cleaned_data['price_high_insurance_security_surcharge']
    
    min_fuel_surcharge = form3.cleaned_data['min_fuel_surcharge']
    price_fuel_surcharge = form3.cleaned_data['price_fuel_surcharge']
    price_high_fuel_surcharge = form3.cleaned_data['price_high_fuel_surcharge']
    
    min_import_handling_charges = form3.cleaned_data['min_import_handling_charges']
    price_import_handling_charges = form3.cleaned_data['price_import_handling_charges']
    price_high_import_handling_charges = form3.cleaned_data['price_high_import_handling_charges']
    
    
    min_gst_zero_rated = form3.cleaned_data['min_gst_zero_rated']
    price_gst_zero_rated = form3.cleaned_data['price_gst_zero_rated']
    price_high_gst_zero_rated = form3.cleaned_data['price_high_gst_zero_rated']
    
    ### fs and 
    
    prm = ParameterData(products = dt,j_vendor =2,status_param = 1,tgl_aktif_param= datetime.date.today(),cu=user,
        min_express_wordwide_nondoc =min_express_wordwide_nondoc,price_express_wordwide_nondoc =price_express_wordwide_nondoc,
        price_high_express_wordwide_nondoc =price_high_express_wordwide_nondoc,
        min_fuel_surcharge_dhl = min_fuel_surcharge_dhl,
        price_fuel_surcharge_dhl = price_fuel_surcharge_dhl,
        price_high_fuel_surcharge_dhl = price_high_fuel_surcharge_dhl,
        min_emergency_situation = min_emergency_situation,
        price_emergency_situation = price_emergency_situation,
        price_high_emergency_situation = price_high_emergency_situation,
        ##dl
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
        price_gst_zero_rated = price_gst_zero_rated,
        )
    prm.save()
    