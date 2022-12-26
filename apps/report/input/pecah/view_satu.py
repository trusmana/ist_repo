from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.conf import settings

from apps.products import models as mp
from django import forms as fdjango
from apps.report.input import forms as fi

####SING FS DPS SL DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_enam(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,'ssssssss')   # type: ignore      
    if request.method == "POST":
        form = fi.FSForm(request.POST)
        forms = fi.DHLForm(request.POST)
        formss = fi.DLForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid():
            ##fi.FSForm
            tgl_fs = form.cleaned_data['tgl_fs']
            no_invoice_fs = form.cleaned_data['no_invoice_fs']
            qt_fs = form.cleaned_data['qt_fs']
            products = form.cleaned_data['products']
            commodity = form.cleaned_data['commodity']
            param = form.cleaned_data['param']
            
            weight_fs = form.cleaned_data['weight_fs']
            airfreight = form.cleaned_data['price_airfreight']
            price_handling_charges = form.cleaned_data['price_handling_charges']
            price_insurance_security_surcharge = form.cleaned_data['price_insurance_security_surcharge']
            price_fuel_surcharge = form.cleaned_data['price_fuel_surcharge']
            price_import_handling_charges = form.cleaned_data['price_import_handling_charges']
            price_gst_zero_rated = form.cleaned_data['price_gst_zero_rated']

            
            ##fi.DHLForm
            tgl_dhl = forms.cleaned_data['tgl_dhl']
            no_invoice_dhl = forms.cleaned_data['no_invoice_dhl']
            express_wordwide_nondoc = forms.cleaned_data['express_wordwide_nondoc']
            fuel_surcharge_dhl = forms.cleaned_data['fuel_surcharge_dhl']
            emergency_situation = forms.cleaned_data['emergency_situation']

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']

            delivey_to = formss.cleaned_data['delivey_to']
            price_delivey_to_okusi = formss.cleaned_data['price_delivey_to_okusi']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_delivey_to_betano = formss.cleaned_data['price_delivey_to_betano']

            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']

            ####Sale
            
            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
                airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
                import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
            job.save()
            job1 = mp.Job(transaksi= tran,tanggal_invoice =tgl_dhl,no_invoice =no_invoice_dhl,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                express_wordwide_nondoc = express_wordwide_nondoc,fuel_surcharge_dhl = fuel_surcharge_dhl,emergency_situation = emergency_situation,)
            job1.save()
            job2 = mp.Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                delivey_to_betano = price_delivey_to_betano,delivey_to_okusi= price_delivey_to_okusi,
                delivey_to= delivey_to,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        form = fi.FSForm(initial={'tgl_fs':datetime.date.today(),'products':param.products.id,'param':param.id})# type: ignore
        forms = fi.DHLForm(initial={'tgl_dhl':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        form.fields["products"].widget = fdjango.HiddenInput()
        form.fields["param"].widget = fdjango.HiddenInput()
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,
        'forms':forms,'formss':formss,})


####SING FS DPS SL DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_satu(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,'ssssssss')   # type: ignore
    if request.method == "POST":
        form = fi.FSForm(request.POST)
        forms = fi.SLForm(request.POST)
        formss = fi.DLForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() :
            ##fi.FSForm
            tgl_fs = form.cleaned_data['tgl_fs']
            no_invoice_fs = form.cleaned_data['no_invoice_fs']
            qt_fs = form.cleaned_data['qt_fs']
            products = form.cleaned_data['products']
            commodity = form.cleaned_data['commodity']
            param = form.cleaned_data['param']
            
            weight_fs = form.cleaned_data['weight_fs']
            airfreight = form.cleaned_data['price_airfreight']
            price_handling_charges = form.cleaned_data['price_handling_charges']
            price_insurance_security_surcharge = form.cleaned_data['price_insurance_security_surcharge']
            price_fuel_surcharge = form.cleaned_data['price_fuel_surcharge']
            price_import_handling_charges = form.cleaned_data['price_import_handling_charges']
            price_gst_zero_rated = form.cleaned_data['price_gst_zero_rated']

            
            ###fi.SLFORM
            tgl_sl = forms.cleaned_data['tgl_sl']
            no_invoice_sl = forms.cleaned_data['no_invoice_sl']
            no_invoice_sl_2 = forms.cleaned_data['no_invoice_sl_2']
            no_invoice_sl_3 = forms.cleaned_data['no_invoice_sl_3']
            #qt_sl = forms.cleaned_data['qt_sl']
            price_storage_at_cost = forms.cleaned_data['price_storage_at_cost']
            price_pjkp2u_sin_dps_at_cost = forms.cleaned_data['price_pjkp2u_sin_dps_at_cost']
            price_storage_mcl_e_0389249_at_cost = forms.cleaned_data['price_storage_mcl_e_0389249_at_cost']
            price_pjkp2u_dps_dil_at_cost = forms.cleaned_data['price_pjkp2u_dps_dil_at_cost']
            price_airfreight_charges = forms.cleaned_data['price_airfreight_charges']
            price_overweight_charges_surcharge = forms.cleaned_data['price_overweight_charges_surcharge']
            price_awb_fee = forms.cleaned_data['price_awb_fee']
            price_handling_charges_sl = forms.cleaned_data['price_handling_charges_sl']

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']

            delivey_to = formss.cleaned_data['delivey_to']
            price_delivey_to_okusi = formss.cleaned_data['price_delivey_to_okusi']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_delivey_to_betano = formss.cleaned_data['price_delivey_to_betano']

            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']

            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
                airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
                import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
            job.save()
            job1 = mp.Job(transaksi = tran,tanggal_invoice = tgl_sl,no_invoice = no_invoice_sl,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,no_invoice_sl_2 = no_invoice_sl_2,no_invoice_sl_3 = no_invoice_sl_3,# type: ignore
                storage_at_cost = price_storage_at_cost,pjkp2u_sin_dps_at_cost = price_pjkp2u_sin_dps_at_cost,
                storage_mcl_e_0389249_at_cost = price_storage_mcl_e_0389249_at_cost,pjkp2u_dps_dil_at_cost = price_pjkp2u_dps_dil_at_cost,
                airfreight = price_airfreight_charges,overweight_charges_surcharge = price_overweight_charges_surcharge,
                awb_fee = price_awb_fee,handling_charges = price_handling_charges_sl)
            job1.save()
            job2 = mp.Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                delivey_to_betano = price_delivey_to_betano,delivey_to_okusi= price_delivey_to_okusi,
                delivey_to= delivey_to,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        form = fi.FSForm(initial={'tgl_fs':datetime.date.today(),'products':param.products.id,'param':param.id})# type: ignore
        forms = fi.SLForm(initial={'tgl_sl':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        form.fields["products"].widget = fdjango.HiddenInput()
        form.fields["param"].widget = fdjango.HiddenInput()
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,
        'forms':forms,'formss':formss})

####ID  GS sub lintas negara DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_dua(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    if request.method == "POST":
        trsform = fi.TransaksiForm(request.POST)
        form = fi.GastiAsihForm(request.POST)
        forms = fi.LintasNegaraForm(request.POST)
        formss = fi.DLForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and trsform.is_valid():
            products = trsform.cleaned_data['products']
            commodity = trsform.cleaned_data['commodity']
            param = trsform.cleaned_data['param']
            qt_fs = trsform.cleaned_data['qt_fs']
            weight_fs = trsform.cleaned_data['qt_fs']
            
            ###Gastiasih 
            tgl_ga = form.cleaned_data['tgl_ga']           
            no_invoice_ga = form.cleaned_data['no_invoice_ga']
            paking =  form.cleaned_data['paking']
            jenis = form.cleaned_data['jenis']
            amount = form.cleaned_data['amount']

            ###LINTAS NEGARA
            tgl_ln = forms.cleaned_data['tgl_ln']
            no_invoice_ln = forms.cleaned_data['no_invoice_ln']
            transit_charge = forms.cleaned_data['transit_charge']
            transportations_charge = forms.cleaned_data['transportations_charge']

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']
           
            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
            tran.no_pekerjaan = tran._no_pk_()# type: ignore
            tran.save()
            ### gastiasih
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
                pcs = qt_fs,weight =weight_fs,paking =paking,jenis =jenis,amount =amount,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_ln,no_invoice = no_invoice_ln,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,transportations_charge=transportations_charge,transit_charge=transit_charge)# type: ignore
            job1.save()
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()# type: ignore
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = fi.TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = fi.GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = fi.LintasNegaraForm(initial={'tgl_ln':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        trsform.fields["products"].widget = fdjango.HiddenInput()
        trsform.fields["param"].widget = fdjango.HiddenInput()    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'trsform':trsform,
        'forms':forms,'formss':formss})


####ID  GS sub Antarlapan  DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_tiga(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,pse,'ssssssssssssssssss')   # type: ignore
      
    if request.method == "POST":
        trsform = fi.TransaksiForm(request.POST)
        form = fi.GastiAsihForm(request.POST)
        forms = fi.AntarLapanForm(request.POST)
        formss = fi.DLForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and trsform.is_valid():
            products = trsform.cleaned_data['products']
            commodity = trsform.cleaned_data['commodity']
            param = trsform.cleaned_data['param']
            
            qt_fs = trsform.cleaned_data['qt_fs']
            weight_fs = trsform.cleaned_data['qt_fs']
            
            ###Gastiasih            
            tgl_ga = form.cleaned_data['tgl_ga']           
            no_invoice_ga = form.cleaned_data['no_invoice_ga']
            paking =  form.cleaned_data['paking']
            jenis = form.cleaned_data['jenis']
            amount = form.cleaned_data['amount']
            ###Gastiasih

            ###Antarlapan
            tgl_al = forms.cleaned_data['tgl_al']
            no_invoice_al = forms.cleaned_data['no_invoice_al']
            cbm = forms.cleaned_data['cbm']
            twentyft = forms.cleaned_data['twentyft']
            blfee = forms.cleaned_data['blfee']
            biaya_peb = forms.cleaned_data['biaya_peb']
            ###Antarlapan

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']
            #fi.DLFORM

            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### gastiasih
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
                pcs = qt_fs,weight =weight_fs,paking =paking,jenis =jenis,amount =amount,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### Antarlapan
            job1 = mp.Job(transaksi = tran,tanggal_invoice = tgl_al,no_invoice = no_invoice_al,
                nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,# type: ignore
                cbm = cbm,twentyft = twentyft,blfee = blfee,biaya_peb = biaya_peb,
                )
            job1.save()
            ### Antarlapan
            ###Dili
            job2 = mp.Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = fi.mp.TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = fi.GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = fi.AntarLapanForm(initial={'tgl_al':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        trsform.fields["products"].widget = fdjango.HiddenInput()
        trsform.fields["param"].widget = fdjango.HiddenInput()    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'trsform':trsform,
        'forms':forms,'formss':formss})

####ID  Sing DL ,GASTI  SOLID DILI
@login_required(login_url=settings.LOGIN_URL)
def proses_input_empat(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,pse,'ssssssssssssssssss')   # type: ignore
      
    if request.method == "POST":
        trsform = fi.TransaksiForm(request.POST)
        form = fi.GastiAsihForm(request.POST)
        forms = fi.SLForm(request.POST)
        formss = fi.DLForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and trsform.is_valid():
            products = trsform.cleaned_data['products']
            commodity = trsform.cleaned_data['commodity']
            param = trsform.cleaned_data['param']
            
            qt_fs = trsform.cleaned_data['qt_fs']
            weight_fs = trsform.cleaned_data['qt_fs']
            
            ###Gastiasih            
            tgl_ga = form.cleaned_data['tgl_ga']           
            no_invoice_ga = form.cleaned_data['no_invoice_ga']
            paking =  form.cleaned_data['paking']
            jenis = form.cleaned_data['jenis']
            amount = form.cleaned_data['amount']
            ###Gastiasih

            ###solid
            tgl_sl = forms.cleaned_data['tgl_sl']
            no_invoice_sl = forms.cleaned_data['no_invoice_sl']
            no_invoice_sl_2 = forms.cleaned_data['no_invoice_sl_2']
            no_invoice_sl_3 = forms.cleaned_data['no_invoice_sl_3']
            #qt_sl = forms.cleaned_data['qt_sl']
            price_storage_at_cost = forms.cleaned_data['price_storage_at_cost']
            price_pjkp2u_sin_dps_at_cost = forms.cleaned_data['price_pjkp2u_sin_dps_at_cost']
            price_storage_mcl_e_0389249_at_cost = forms.cleaned_data['price_storage_mcl_e_0389249_at_cost']
            price_pjkp2u_dps_dil_at_cost = forms.cleaned_data['price_pjkp2u_dps_dil_at_cost']
            price_airfreight_charges = forms.cleaned_data['price_airfreight_charges']
            price_overweight_charges_surcharge = forms.cleaned_data['price_overweight_charges_surcharge']
            price_awb_fee = forms.cleaned_data['price_awb_fee']
            price_handling_charges_sl = forms.cleaned_data['price_handling_charges_sl']
            ###solid

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']
            #fi.DLFORM

            
            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### gastiasih
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
                pcs = qt_fs,weight =weight_fs,paking =paking,jenis =jenis,amount =amount,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### Solid
            job1 = mp.Job(transaksi = tran,tanggal_invoice = tgl_sl,no_invoice = no_invoice_sl,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,no_invoice_sl_2 = no_invoice_sl_2,no_invoice_sl_3 = no_invoice_sl_3,# type: ignore
                storage_at_cost = price_storage_at_cost,pjkp2u_sin_dps_at_cost = price_pjkp2u_sin_dps_at_cost,
                storage_mcl_e_0389249_at_cost = price_storage_mcl_e_0389249_at_cost,pjkp2u_dps_dil_at_cost = price_pjkp2u_dps_dil_at_cost,
                airfreight = price_airfreight_charges,overweight_charges_surcharge = price_overweight_charges_surcharge,
                awb_fee = price_awb_fee,handling_charges = price_handling_charges_sl
                )
            job1.save()
            ### Solid
            ###Dili
            job2 = mp.Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = fi.mp.TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = fi.GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = fi.SLForm(initial={'tgl_sl':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        trsform.fields["products"].widget = fdjango.HiddenInput()
        trsform.fields["param"].widget = fdjango.HiddenInput()    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'trsform':trsform,
        'forms':forms,'formss':formss})

####ND  Sing DL ,GASTI Fread DILI
@login_required(login_url=settings.LOGIN_URL)
def proses_input_lima(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = mp.ParameterData.objects.get(id = param)
    
    if request.method == "POST":
        trsform = fi.TransaksiForm(request.POST)
        form = fi.WarsilaForm(request.POST)
        forms = fi.FSForm(request.POST)
        formss = fi.DLForm(request.POST)
        
        if form.is_valid() and forms.is_valid() and formss.is_valid() and trsform.is_valid():
            products = trsform.cleaned_data['products']
            commodity = trsform.cleaned_data['commodity']
            param = trsform.cleaned_data['param']
            
            qt_fs = trsform.cleaned_data['qt_fs']
            weight_fs = trsform.cleaned_data['qt_fs']
            
            ###Wastila belanda 
            tgl_wsl = form.cleaned_data['tgl_wsl']
            no_invoice_wsl = form.cleaned_data['no_invoice_wsl']
            custom_learance_fee_handling =form.cleaned_data['custom_learance_fee_handling']
            heavy_weight_surcharge =form.cleaned_data['heavy_weight_surcharge']
            agent_fee =form.cleaned_data['agent_fee']
            delivery =form.cleaned_data['delivery']
            ###Wastila belanda

            ###Fread
            tgl_fs = forms.cleaned_data['tgl_fs']
            no_invoice_fs = forms.cleaned_data['no_invoice_fs']

            price_airfreight = forms.cleaned_data['price_airfreight']
            price_handling_charges = forms.cleaned_data['price_handling_charges']
            price_insurance_security_surcharge = forms.cleaned_data['price_insurance_security_surcharge']
            price_fuel_surcharge = forms.cleaned_data['price_fuel_surcharge']
            price_import_handling_charges = forms.cleaned_data['price_import_handling_charges']
            price_gst_zero_rated = forms.cleaned_data['price_gst_zero_rated']
            ###fred

            #fi.DLFORM
            tgl_dl = formss.cleaned_data['tgl_dl']
            no_invoice_dl = formss.cleaned_data['no_invoice_dl']
            
            price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
            price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
            price_custom_clearance = formss.cleaned_data['price_custom_clearance']
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']
            #fi.DLFORM
            tran = mp.Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### Wastila
            job = mp.Job(transaksi= tran,tanggal_invoice =tgl_wsl,no_invoice = no_invoice_wsl,# type: ignore
                pcs = qt_fs,# type: ignore
                custom_learance_fee_handling =custom_learance_fee_handling,
                heavy_weight_surcharge =heavy_weight_surcharge,agent_fee =agent_fee,delivery =delivery,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### fred
            job1 = mp.Job(transaksi = tran,tanggal_invoice = tgl_fs,no_invoice = no_invoice_fs,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,# type: ignore
                airfreight = price_airfreight,handling_charges = price_handling_charges, 
                insurance_security_surcharge = price_insurance_security_surcharge, 
                fuel_surcharge = price_fuel_surcharge, 
                import_handling_charges = price_import_handling_charges, 
                gst_zero_rated = price_gst_zero_rated)
            job1.save()
            ### fred
            ###Dili
            job2 = mp.Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = fi.mp.TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = fi.WarsilaForm(initial={'tgl_wsl':datetime.date.today()})
        forms = fi.FSForm(initial={'tgl_fs':datetime.date.today()})
        formss = fi.DLForm(initial={'tgl_dl':datetime.date.today()})
        trsform.fields["products"].widget = fdjango.HiddenInput()
        trsform.fields["param"].widget = fdjango.HiddenInput()
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'trsform':trsform,
        'forms':forms,'formss':formss})