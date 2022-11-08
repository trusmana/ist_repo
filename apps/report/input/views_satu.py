from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from apps.products.models import Job, ParameterData, ParameterDataBl, Sale, Transaksi
from .forms import PengajuanForm,FSForm,SLForm,DLForm,SALEForm

@login_required(login_url=settings.LOGIN_URL)
def proses_input_satu(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products) 
      
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
            price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
            price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
            price_handling_fee = formss.cleaned_data['price_handling_fee']
            admin_fee = formss.cleaned_data['admin_fee']
            fee_collection = formss.cleaned_data['fee_collection']

            ####Sale
            paramsale = slforms.cleaned_data['paramsale']
            re_export_shipment_one = slforms.cleaned_data['re_export_shipment_one']
            re_export_shipment_one_pcs = slforms.cleaned_data['re_export_shipment_one_pcs']
            re_export_shipment_one_qty = slforms.cleaned_data['re_export_shipment_one_qty']

            re_export_shipment_two = slforms.cleaned_data['re_export_shipment_two']
            re_export_shipment_two_pcs = slforms.cleaned_data['re_export_shipment_two_pcs']
            re_export_shipment_two_qty = slforms.cleaned_data['re_export_shipment_two_qty']

            cartage_warehouse_charge_one = slforms.cleaned_data['cartage_warehouse_charge_one']
            airfreight_one = slforms.cleaned_data['airfreight_one']
            cartage_warehouse_charge_two = slforms.cleaned_data['cartage_warehouse_charge_two']
            airfreight_two = slforms.cleaned_data['airfreight_two']
            export_handling_sale = slforms.cleaned_data['export_handling_sale']
            freight_sale = slforms.cleaned_data['freight_sale']
            doc_clearance_sale = slforms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = slforms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = slforms.cleaned_data['warehouse_charge_sale']
            handling_charge_sale = slforms.cleaned_data['handling_charge_sale']
            delivery_sale = slforms.cleaned_data['delivery_sale']
            duty_tax_sale = slforms.cleaned_data['duty_tax_sale']
            tax_handling_charge_sale = slforms.cleaned_data['tax_handling_charge_sale']
            tran = Transaksi(tanggal= sekarang,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,
                re_export_shipment_one=re_export_shipment_one,re_export_shipment_one_pcs=re_export_shipment_one_pcs,
                re_export_shipment_one_qty=re_export_shipment_one_qty,re_export_shipment_two=re_export_shipment_two,
                re_export_shipment_two_pcs=re_export_shipment_two_pcs,re_export_shipment_two_qty=re_export_shipment_two_qty)
            tran.no_pekerjaan = tran._no_pk_()
            tran.save()
            job = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
                airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,
                vendor = tran.products.origin_vendor,
                insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
                import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
            job.save()
            job1 = Job(transaksi = tran,tanggal_invoice = tgl_sl,no_invoice = no_invoice_sl,nilai_kurs = tran.products.kurs_through,
                vendor = tran.products.through_vendor,
                storage_at_cost = price_storage_at_cost,pjkp2u_sin_dps_at_cost = price_pjkp2u_sin_dps_at_cost,
                storage_mcl_e_0389249_at_cost = price_storage_mcl_e_0389249_at_cost,pjkp2u_dps_dil_at_cost = price_pjkp2u_dps_dil_at_cost,
                airfreight = price_airfreight_charges,overweight_charges_surcharge = price_overweight_charges_surcharge,
                awb_fee = price_awb_fee,handling_charges = price_handling_charges_sl)
            job1.save()
            job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,
                vendor = tran.products.destinations_vendor,
                ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
                custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
                akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
                admin_fee = admin_fee,fee_collection = fee_collection)
            job2.save()
            sale = Sale(trans=tran,prod=paramsale,cu=user,cartage_warehouse_charge_one = cartage_warehouse_charge_one,airfreight_one = airfreight_one,
                cartage_warehouse_charge_two = cartage_warehouse_charge_two,airfreight_two = airfreight_two,
                export_handling = export_handling_sale,freight =freight_sale,
                doc_clearance = doc_clearance_sale,ground_handling = ground_handling_sale,
                warehouse_charge = warehouse_charge_sale,handling_charge = handling_charge_sale,
                delivery= delivery_sale,duty_tax = duty_tax_sale,tax_handling_charge = tax_handling_charge_sale)
            sale.save()    
            messages.success(request, 'Job Berhasil Di simpan')
            return redirect('d-job')            
    else:
        form = FSForm(initial={'tgl_fs':datetime.date.today(),'products':param.products.id,'param':param.id})
        forms = SLForm(initial={'tgl_sl':datetime.date.today()})
        formss = DLForm(initial={'tgl_dl':datetime.date.today()})
        slforms = SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})
    
    return render(request,'pengajuan/input/proses_input_satu.html',{'param':param,'form':form,'pse':pse,
        'forms':forms,'formss':formss,'sl':slforms})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_simulasi_form_satu(request, h_ajax, template_name):
    data = dict()
    context = {'h_ajax': h_ajax}
    data['django_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def showparamsatu(request):
    jenis_produk = request.GET.get('jenis_produk',None)
    produk = request.GET.get('produk',None)
    tanggal = request.GET.get('tanggal',None)
    poin_tiga = request.GET.get('poin_tiga',None)
    destinations_vendor = request.GET.get('destinations_vendor',None)    
    
    param = ParameterData.objects.get(products=produk,products__point_tiga=poin_tiga,
        products__destinations_vendor=destinations_vendor,products__status=1,products__jenis_produk=jenis_produk)
    prd = param.products.kode_produk    
    h_ajax ={'tanggal':tanggal,'produk':prd,'param':param.id,'ds_ven':param.products.through_vendor,
        'ds': param.products.point_dua,'lt_ven':param.products.destinations_vendor,'lt':param.products.point_tiga,
        'js':param.products.jenis_produk,'jmlv':param.products.jumlah_vendor }
    return save_simulasi_form_satu(request, h_ajax,'pengajuan/addpengajuan_satu.html')
    