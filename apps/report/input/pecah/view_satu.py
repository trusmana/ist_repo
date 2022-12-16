from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.conf import settings

from apps.products.models import Job, ParameterData, ParameterDataBl, Sale, Transaksi
from apps.report.input.forms import FSForm,SLForm,DLForm,SALEForm,DHLForm,\
    GastiAsihForm,LintasNegaraForm,AntarLapanForm,TransaksiForm,WarsilaForm

####SING FS DPS SL DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_enam(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,'ssssssss')   # type: ignore      
    if request.method == "POST":
        form = FSForm(request.POST)
        forms = DHLForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid():
            ##FSForm
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

            
            ##DHLForm
            tgl_dhl = forms.cleaned_data['tgl_dhl']
            no_invoice_dhl = forms.cleaned_data['no_invoice_dhl']
            express_wordwide_nondoc = forms.cleaned_data['express_wordwide_nondoc']
            fuel_surcharge_dhl = forms.cleaned_data['fuel_surcharge_dhl']
            emergency_situation = forms.cleaned_data['emergency_situation']

            #DLFORM
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
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']            
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']
            
            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']


            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            job = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
                airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
                import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
            job.save()
            job1 = Job(transaksi= tran,tanggal_invoice =tgl_dhl,no_invoice =no_invoice_dhl,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                express_wordwide_nondoc = express_wordwide_nondoc,fuel_surcharge_dhl = fuel_surcharge_dhl,emergency_situation = emergency_situation,)
            job1.save()
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                delivey_to_betano = price_delivey_to_betano,delivey_to_okusi= price_delivey_to_okusi,
                delivey_to= delivey_to,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                warehouse_charge_days = warehouse_charge_days,
                price_delivery = price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,status_duty= status_duty,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        form = FSForm(initial={'tgl_fs':datetime.date.today(),'products':param.products.id,'param':param.id})# type: ignore
        forms = DHLForm(initial={'tgl_dhl':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})# type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,
        'forms':forms,'formss':formss,'sl':slforms})


####SING FS DPS SL DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_satu(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,'ssssssss')   # type: ignore
      
    if request.method == "POST":
        form = FSForm(request.POST)
        forms = SLForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid():
            ##FSForm
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

            
            ###SLFORM
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

            #DLFORM
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
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']

            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            job = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
                airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
                vendor = tran.products.origin_vendor,# type: ignore
                insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
                import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
            job.save()
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_sl,no_invoice = no_invoice_sl,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,no_invoice_sl_2 = no_invoice_sl_2,no_invoice_sl_3 = no_invoice_sl_3,# type: ignore
                storage_at_cost = price_storage_at_cost,pjkp2u_sin_dps_at_cost = price_pjkp2u_sin_dps_at_cost,
                storage_mcl_e_0389249_at_cost = price_storage_mcl_e_0389249_at_cost,pjkp2u_dps_dil_at_cost = price_pjkp2u_dps_dil_at_cost,
                airfreight = price_airfreight_charges,overweight_charges_surcharge = price_overweight_charges_surcharge,
                awb_fee = price_awb_fee,handling_charges = price_handling_charges_sl)
            job1.save()
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                delivey_to_betano = price_delivey_to_betano,delivey_to_okusi= price_delivey_to_okusi,
                delivey_to= delivey_to,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                warehouse_charge_days = warehouse_charge_days,
                price_delivery = price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,status_duty= status_duty,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        form = FSForm(initial={'tgl_fs':datetime.date.today(),'products':param.products.id,'param':param.id})# type: ignore
        forms = SLForm(initial={'tgl_sl':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})# type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,
        'forms':forms,'formss':formss,'sl':slforms})

####ID  GS sub lintas negara DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_dua(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
      
    if request.method == "POST":
        trsform = TransaksiForm(request.POST)
        form = GastiAsihForm(request.POST)
        forms = LintasNegaraForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid() and trsform.is_valid():
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

            #DLFORM
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

            ####Sale
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']

            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()# type: ignore
            tran.save()
            ### gastiasih
            job = Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
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
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                warehouse_charge_days = warehouse_charge_days,
                price_delivery = price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,status_duty=status_duty,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = LintasNegaraForm(initial={'tgl_ln':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})  # type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,'trsform':trsform,
        'forms':forms,'formss':formss,'sl':slforms})


####ID  GS sub Antarlapan  DIl DIL 
@login_required(login_url=settings.LOGIN_URL)
def proses_input_tiga(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,pse,'ssssssssssssssssss')   # type: ignore
      
    if request.method == "POST":
        trsform = TransaksiForm(request.POST)
        form = GastiAsihForm(request.POST)
        forms = AntarLapanForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid() and trsform.is_valid():
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

            #DLFORM
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
            #DLFORM

            ####Sale
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']

            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            status_duty = slforms.cleaned_data['status_duty']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### gastiasih
            job = Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
                pcs = qt_fs,weight =weight_fs,paking =paking,jenis =jenis,amount =amount,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### Antarlapan
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_al,no_invoice = no_invoice_al,
                nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,# type: ignore
                cbm = cbm,twentyft = twentyft,blfee = blfee,biaya_peb = biaya_peb,
                )
            job1.save()
            ### Antarlapan
            ###Dili
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                warehouse_charge_days = warehouse_charge_days,
                price_delivery= price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,status_duty=status_duty,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = AntarLapanForm(initial={'tgl_al':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})  # type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,'trsform':trsform,
        'forms':forms,'formss':formss,'sl':slforms})

####ID  Sing DL ,GASTI  SOLID DILI
@login_required(login_url=settings.LOGIN_URL)
def proses_input_empat(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
    print(pse,'Cekk')
    print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,pse,'ssssssssssssssssss')   # type: ignore
      
    if request.method == "POST":
        trsform = TransaksiForm(request.POST)
        form = GastiAsihForm(request.POST)
        forms = SLForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid() and trsform.is_valid():
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

            #DLFORM
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
            #DLFORM

            ####Sale
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']

            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            status_duty = slforms.cleaned_data['status_duty']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### gastiasih
            job = Job(transaksi= tran,tanggal_invoice =tgl_ga,no_invoice = no_invoice_ga,
                pcs = qt_fs,weight =weight_fs,paking =paking,jenis =jenis,amount =amount,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### Solid
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_sl,no_invoice = no_invoice_sl,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,no_invoice_sl_2 = no_invoice_sl_2,no_invoice_sl_3 = no_invoice_sl_3,# type: ignore
                storage_at_cost = price_storage_at_cost,pjkp2u_sin_dps_at_cost = price_pjkp2u_sin_dps_at_cost,
                storage_mcl_e_0389249_at_cost = price_storage_mcl_e_0389249_at_cost,pjkp2u_dps_dil_at_cost = price_pjkp2u_dps_dil_at_cost,
                airfreight = price_airfreight_charges,overweight_charges_surcharge = price_overweight_charges_surcharge,
                awb_fee = price_awb_fee,handling_charges = price_handling_charges_sl
                )
            job1.save()
            ### Solid
            ###Dili
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                warehouse_charge_days = warehouse_charge_days,
                price_delivery = price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,status_duty=status_duty,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = GastiAsihForm(initial={'tgl_ga':datetime.date.today()})
        forms = SLForm(initial={'tgl_sl':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})  # type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,'trsform':trsform,
        'forms':forms,'formss':formss,'sl':slforms})

####ND  Sing DL ,GASTI Fread DILI
@login_required(login_url=settings.LOGIN_URL)
def proses_input_lima(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products)
    print(pse,'Sale')
    #print(param.products.origin_vendor.id,param.products.through_vendor.id,param.products.destinations_vendor.id,pse,'ssssssssssssssssss')   # type: ignore
      
    if request.method == "POST":
        trsform = TransaksiForm(request.POST)
        form = WarsilaForm(request.POST)
        forms = FSForm(request.POST)
        formss = DLForm(request.POST)
        slforms = SALEForm(request.POST)
        if form.is_valid() and forms.is_valid() and formss.is_valid() and slforms.is_valid() and trsform.is_valid():
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

            #DLFORM
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
            #DLFORM

            ####Sale
            paramsale = slforms.cleaned_data['paramsale']
            total_shipment = slforms.cleaned_data['total_shipment']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            awb = slforms.cleaned_data['awb']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            re_export_shipment_tree = slforms.cleaned_data['re_export_shipment_tree']
            re_export_shipment_tree_pcs = slforms.cleaned_data['re_export_shipment_tree_pcs']
            re_export_shipment_tree_qty = slforms.cleaned_data['re_export_shipment_tree_qty']

            re_export_shipment_four = slforms.cleaned_data['re_export_shipment_four']
            re_export_shipment_four_pcs = slforms.cleaned_data['re_export_shipment_four_pcs']
            re_export_shipment_four_qty = slforms.cleaned_data['re_export_shipment_four_qty']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            cartage_warehouse_charge_tree = slforms.cleaned_data['cartage_warehouse_charge_tree']
            airfreight_tree = slforms.cleaned_data['airfreight_tree']
            cartage_warehouse_charge_four = slforms.cleaned_data['cartage_warehouse_charge_four']
            airfreight_four = slforms.cleaned_data['airfreight_four']

            price_cartage_warehouse_charge_one =slforms.cleaned_data['price_cartage_warehouse_charge_one']
            price_cartage_warehouse_charge_two =slforms.cleaned_data['price_cartage_warehouse_charge_two']
            price_cartage_warehouse_charge_tree =slforms.cleaned_data['price_cartage_warehouse_charge_tree']
            price_cartage_warehouse_charge_four =slforms.cleaned_data['price_cartage_warehouse_charge_four']
            price_doc_clearance_sale = slforms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = slforms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = slforms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = slforms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = slforms.cleaned_data['price_delivery_sale']
            price_freight_sale = slforms.cleaned_data['price_freight_sale']


            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = slforms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            status_duty = slforms.cleaned_data['status_duty']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            status_duty = slforms.cleaned_data['status_duty']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            shipment_value = slforms.cleaned_data['shipment_value']
            insurance = slforms.cleaned_data['insurance']
            eta = slforms.cleaned_data['eta']
            etd = slforms.cleaned_data['etd']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty,
                re_export_shipment_tree=re_export_shipment_tree,
                re_export_shipment_tree_pcs=re_export_shipment_tree_pcs,re_export_shipment_tree_qty=re_export_shipment_tree_qty,
                re_export_shipment_four=re_export_shipment_four,
                re_export_shipment_four_pcs=re_export_shipment_four_pcs,re_export_shipment_four_qty=re_export_shipment_four_qty)
            tran.no_pekerjaan = tran._no_pk_()  # type: ignore
            tran.save()
            ### Wastila
            job = Job(transaksi= tran,tanggal_invoice =tgl_wsl,no_invoice = no_invoice_wsl,# type: ignore
                pcs = qt_fs,# type: ignore
                custom_learance_fee_handling =custom_learance_fee_handling,
                heavy_weight_surcharge =heavy_weight_surcharge,agent_fee =agent_fee,delivery =delivery,
                vendor = tran.products.origin_vendor,nilai_kurs = tran.products.kurs_origin)# type: ignore
            job.save()
            ### fred
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_fs,no_invoice = no_invoice_fs,nilai_kurs = tran.products.kurs_through,# type: ignore
                vendor = tran.products.through_vendor,# type: ignore
                airfreight = price_airfreight,handling_charges = price_handling_charges, 
                insurance_security_surcharge = price_insurance_security_surcharge, 
                fuel_surcharge = price_fuel_surcharge, 
                import_handling_charges = price_import_handling_charges, 
                gst_zero_rated = price_gst_zero_rated)
            job1.save()
            ### fred
            ###Dili
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
                vendor = tran.products.destinations_vendor,# type: ignore
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            ###dili
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                cartage_warehouse_charge_tree = cartage_warehouse_charge_tree,airfreight_tree = airfreight_tree,
                cartage_warehouse_charge_four = cartage_warehouse_charge_four,airfreight_four = airfreight_four,
                total_shipment=total_shipment,
                price_cartage_warehouse_charge_one =price_cartage_warehouse_charge_one,
                price_cartage_warehouse_charge_two =price_cartage_warehouse_charge_two,
                price_cartage_warehouse_charge_tree =price_cartage_warehouse_charge_tree,
                price_cartage_warehouse_charge_four =price_cartage_warehouse_charge_four,
                price_doc_clearance = price_doc_clearance_sale,
                price_ground_handling = price_ground_handling_sale,
                price_warehouse_charge = price_warehouse_charge_sale,
                price_handling_charge = price_handling_charge_sale,
                price_delivery = price_delivery_sale,price_freight = price_freight_sale,
                export_handling = export_handling_sale,freight =freight_sale,status_duty=status_duty,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge_days = warehouse_charge_days,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale,
                eta=eta,etd=etd,awb=awb,shipment_value=shipment_value,insurance=insurance)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
        form = WarsilaForm(initial={'tgl_wsl':datetime.date.today()})
        forms = FSForm(initial={'tgl_fs':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})  # type: ignore
    
    return render(request,'pengajuan/input/pecah/proses_input_tiga.html',{'param':param,'form':form,'pse':pse,'trsform':trsform,
        'forms':forms,'formss':formss,'sl':slforms})