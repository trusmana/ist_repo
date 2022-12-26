from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from apps.products.models import Job, ParameterData, ParameterDataBl, Sale, Transaksi,Produk
from .forms import FSForm,DLForm,DHLForm,TransaksiForm

@login_required(login_url=settings.LOGIN_URL)
def proses_input_dua_vendor(request,param):
    user = request.user
    sekarang = datetime.date.today()
    param = ParameterData.objects.get(id = param)
    pse = ParameterDataBl.objects.get(products = param.products) 
    dt = Produk.objects.get(id=param.products.id)
    print(param.products.origin_vendor.id,param.products.destinations_vendor.id,'cek')
    ## FS - DILI
    if param.products.origin_vendor.id == 5 and param.products.destinations_vendor.id == 1:
        if request.method == "POST":
            trsform = TransaksiForm(request.POST) #### digunakan Khusus Yg Bukan Fred vendor
            form = DLForm(request.POST)###satu
            formss = FSForm(request.POST)###Tiga
            if trsform.is_valid() and form.is_valid() and formss.is_valid() :
                save_dili_fr_indah(dt,form,formss,trsform,user)
                messages.success(request, 'Job Berhasil Di simpan')
                return redirect('d-job')
        else:
            trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
            form = DLForm(initial={'tgl_dl':sekarang})
            formss = FSForm(initial={'tgl_fs':sekarang})
            return render(request,'pengajuan/input/proses_input_dua.html',{'form':form,'formss':formss,
                'trsform':trsform,'dt':dt,'pse':pse})
    ###Dili - Fr    
    if param.products.origin_vendor.id == 1 and param.products.destinations_vendor.id == 5:
        if request.method == "POST":
            trsform = TransaksiForm(request.POST)
            form = FSForm(request.POST)###satu
            formss = DLForm(request.POST)###Tiga
            
            if trsform.is_valid() and form.is_valid() and formss.is_valid():
                save_fr_dili_indah(dt,form,formss,trsform,user)
                messages.success(request, 'Data Job Berhasil Di Input')
                return redirect('d-job')
        else:
            trsform = TransaksiForm()
            form = FSForm(initial={'tgl_fs':sekarang,'products':param.products.id,'param':param.id})  # type: ignore
            formss = DLForm(initial={'tgl_dl':sekarang})
            return render(request,'pengajuan/input/proses_input_dua.html',{'form':form,'formss':formss,
                'trsform':trsform,'dt':dt,'pse':pse})    
    ## DHL - DILI
    if param.products.origin_vendor.id == 8 and param.products.destinations_vendor.id == 5:
        print('kesini')
        if request.method == 'POST':
            trsform = TransaksiForm(request.POST) #### digunakan Khusus Yg Bukan Fred vendor
            form = DHLForm(request.POST)
            formss = DLForm(request.POST)
            if trsform.is_valid() and form.is_valid() and formss.is_valid():
                save_dhl_dili_indah(dt,form,formss,trsform,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-job')
        else:
            trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
            form = DHLForm(initial={'tgl_dhl':sekarang})
            formss = DLForm(initial={'tgl_dl':sekarang})
        return render(request,'pengajuan/input/proses_input_dua.html',{'form':form,'formss':formss,
            'trsform':trsform,'dt':dt,'pse':pse})
    ### DHL FS
    if param.products.origin_vendor.id == 8 and param.products.destinations_vendor.id == 1:
        print('kesinia')
        if request.method == 'POST':
            trsform = TransaksiForm(request.POST) #### digunakan Khusus Yg Bukan Fred vendor
            form = DHLForm(request.POST)
            formss = FSForm(request.POST)
            if trsform.is_valid() and form.is_valid() and formss.is_valid():
                save_dhl_fs_indah(dt,form,formss,trsform,user)
                messages.success(request, 'Data Parameter Berhasil Di Input')
                return redirect('d-job')
        else:
            trsform = TransaksiForm(initial={'products':param.products.id,'param':param.id})  # type: ignore
            form = DHLForm(initial={'tgl_dhl':sekarang})
            formss = FSForm(initial={'tgl_fs':sekarang})
            sl = SALEForm(initial={'tanggal':sekarang,'paramsale':pse.id})  # type: ignore
        return render(request,'pengajuan/input/proses_input_dua.html',{'form':form,'formss':formss,
            'trsform':trsform,'dt':dt,'pse':pse})
        
    return render(request,'pengajuan/input/proses_input_dua.html',{'param':param,'pse':pse,})

def save_dhl_fs_indah(dt,form,formss,trsform,user):
    products = trsform.cleaned_data['products']
    commodity = trsform.cleaned_data['commodity']
    param = trsform.cleaned_data['param']    
    qt_fs = trsform.cleaned_data['qt_fs']    
    
    ##DHLForm
    tgl_dhl = form.cleaned_data['tgl_dhl']
    no_invoice_dhl = form.cleaned_data['no_invoice_dhl']
    express_wordwide_nondoc = form.cleaned_data['express_wordwide_nondoc']
    fuel_surcharge_dhl = form.cleaned_data['fuel_surcharge_dhl']
    emergency_situation = form.cleaned_data['emergency_situation']

    ##FSForm
    tgl_fs = formss.cleaned_data['tgl_fs']
    no_invoice_fs = formss.cleaned_data['no_invoice_fs']
    weight_fs = formss.cleaned_data['weight_fs']
    airfreight = formss.cleaned_data['price_airfreight']
    price_handling_charges = formss.cleaned_data['price_handling_charges']
    price_insurance_security_surcharge = formss.cleaned_data['price_insurance_security_surcharge']
    price_fuel_surcharge = formss.cleaned_data['price_fuel_surcharge']
    price_import_handling_charges = formss.cleaned_data['price_import_handling_charges']
    price_gst_zero_rated = formss.cleaned_data['price_gst_zero_rated']

    tran = Transaksi(tanggal= datetime.date.today,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
    tran.no_pekerjaan = tran._no_pk_()  # type: ignore
    tran.save()
    job = Job(transaksi= tran,tanggal_invoice =tgl_dhl,no_invoice =no_invoice_dhl,nilai_kurs = tran.products.kurs_origin,# type: ignore
        vendor = tran.products.origin_vendor,# type: ignore
        express_wordwide_nondoc = express_wordwide_nondoc,fuel_surcharge_dhl = fuel_surcharge_dhl,emergency_situation = emergency_situation,
        )
    job.save()    
    job2 = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
        airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
        vendor = tran.products.destinations_vendor,# type: ignore
        insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
        import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
    job2.save()    
    


def save_dhl_dili_indah(dt,form,formss,trsform,user):
    products = trsform.cleaned_data['products']
    commodity = trsform.cleaned_data['commodity']
    param = trsform.cleaned_data['param']
    
    qt_fs = trsform.cleaned_data['qt_fs']
    weight_fs = trsform.cleaned_data['weight_fs']
    
    ##DHLForm
    tgl_dhl = form.cleaned_data['tgl_dhl']
    no_invoice_dhl = form.cleaned_data['no_invoice_dhl']
    express_wordwide_nondoc = form.cleaned_data['express_wordwide_nondoc']
    fuel_surcharge_dhl = form.cleaned_data['fuel_surcharge_dhl']
    emergency_situation = form.cleaned_data['emergency_situation']

    #DLFORM
    tgl_dl = formss.cleaned_data['tgl_dl']
    no_invoice_dl = formss.cleaned_data['no_invoice_dl']
    
    price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
    price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
    price_custom_clearance = formss.cleaned_data['price_custom_clearance']
    price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
    price_delivey_to_okusi = formss.cleaned_data['price_delivey_to_okusi']
    price_delivey_to_betano = formss.cleaned_data['price_delivey_to_betano']
    price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
    price_handling_fee = formss.cleaned_data['price_handling_fee']
    admin_fee = formss.cleaned_data['admin_fee']
    fee_collection = formss.cleaned_data['fee_collection']

    
    job = Job(transaksi= tran,tanggal_invoice =tgl_dhl,no_invoice =no_invoice_dhl,nilai_kurs = tran.products.kurs_origin,# type: ignore
        vendor = tran.products.origin_vendor,# type: ignore
        express_wordwide_nondoc = express_wordwide_nondoc,fuel_surcharge_dhl = fuel_surcharge_dhl,emergency_situation = emergency_situation,
        )
    job.save()    
    job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
        vendor = tran.products.destinations_vendor,delivey_to_okusi = price_delivey_to_okusi,delivey_to_betano = price_delivey_to_betano,# type: ignore
        ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
        custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
        akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
        admin_fee = admin_fee,fee_collection = fee_collection)
    job2.save()
    

def save_dili_fr_indah(dt,form,formss,trsform,user):
    products = trsform.cleaned_data['products']
    commodity = trsform.cleaned_data['commodity']
    param = trsform.cleaned_data['param']
    
    qt_fs = trsform.cleaned_data['qt_fs']
    
    ##FSForm
    tgl_fs = formss.cleaned_data['tgl_fs']
    no_invoice_fs = formss.cleaned_data['no_invoice_fs']
    weight_fs = formss.cleaned_data['weight_fs']
    airfreight = formss.cleaned_data['price_airfreight']
    price_handling_charges = formss.cleaned_data['price_handling_charges']
    price_insurance_security_surcharge = formss.cleaned_data['price_insurance_security_surcharge']
    price_fuel_surcharge = formss.cleaned_data['price_fuel_surcharge']
    price_import_handling_charges = formss.cleaned_data['price_import_handling_charges']
    price_gst_zero_rated = formss.cleaned_data['price_gst_zero_rated']           

    #DLFORM
    tgl_dl = form.cleaned_data['tgl_dl']
    no_invoice_dl = form.cleaned_data['no_invoice_dl']
    
    price_ground_handling_dl = form.cleaned_data['price_ground_handling_dl']
    price_forklift_for_heavy_cargo = form.cleaned_data['price_forklift_for_heavy_cargo']
    price_custom_clearance = form.cleaned_data['price_custom_clearance']
    price_delivey_to_hera = form.cleaned_data['price_delivey_to_hera']
    price_delivey_to_okusi = form.cleaned_data['price_delivey_to_okusi']
    price_delivey_to_betano = form.cleaned_data['price_delivey_to_betano']
    price_akses_bandara_inspeksi = form.cleaned_data['price_akses_bandara_inspeksi']
    price_handling_fee = form.cleaned_data['price_handling_fee']
    admin_fee = form.cleaned_data['admin_fee']
    fee_collection = form.cleaned_data['fee_collection']

    
    tran = Transaksi(tanggal= datetime.date.today,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user,)
    tran.no_pekerjaan = tran._no_pk_()  # type: ignore
    tran.save()
    job = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
        airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
        vendor = tran.products.origin_vendor,# type: ignore
        insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
        import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
    job.save()
    
    job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
        vendor = tran.products.destinations_vendor,delivey_to_okusi = price_delivey_to_okusi,delivey_to_betano = price_delivey_to_betano,# type: ignore
        ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
        custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
        akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
        admin_fee = admin_fee,fee_collection = fee_collection)
    job2.save()
    
def save_fr_dili_indah(dt,form,formss,trsform,user):
    ##FSForm
    tgl_fs = form.cleaned_data['tgl_fs']
    products = form.cleaned_data['products']
    commodity = form.cleaned_data['commodity']
    param = form.cleaned_data['param']
    qt_fs = trsform.cleaned_data['qt_fs']
    no_invoice_fs = form.cleaned_data['no_invoice_fs']
    weight_fs = form.cleaned_data['weight_fs']
    airfreight = form.cleaned_data['price_airfreight']
    price_handling_charges = form.cleaned_data['price_handling_charges']
    price_insurance_security_surcharge = form.cleaned_data['price_insurance_security_surcharge']
    price_fuel_surcharge = form.cleaned_data['price_fuel_surcharge']
    price_import_handling_charges = form.cleaned_data['price_import_handling_charges']
    price_gst_zero_rated = form.cleaned_data['price_gst_zero_rated']
    
    #DLFORM
    tgl_dl = formss.cleaned_data['tgl_dl']
    no_invoice_dl = formss.cleaned_data['no_invoice_dl']
    
    price_ground_handling_dl = formss.cleaned_data['price_ground_handling_dl']
    price_forklift_for_heavy_cargo = formss.cleaned_data['price_forklift_for_heavy_cargo']
    price_custom_clearance = formss.cleaned_data['price_custom_clearance']
    price_delivey_to_okusi = formss.cleaned_data['price_delivey_to_okusi']
    price_delivey_to_hera = formss.cleaned_data['price_delivey_to_hera']
    price_delivey_to_betano = formss.cleaned_data['price_delivey_to_betano']
    price_akses_bandara_inspeksi = formss.cleaned_data['price_akses_bandara_inspeksi']
    price_handling_fee = formss.cleaned_data['price_handling_fee']
    admin_fee = formss.cleaned_data['admin_fee']
    fee_collection = formss.cleaned_data['fee_collection']
   
               
    
    tran = Transaksi(tanggal= datetime.date.today,products= products,commodity = commodity ,qty= qt_fs,weight=weight_fs,cu = user)
    tran.no_pekerjaan = tran._no_pk_()  # type: ignore
    tran.save()
    job = Job(transaksi= tran,tanggal_invoice =tgl_fs,no_invoice =no_invoice_fs,
        airfreight = airfreight,handling_charges = price_handling_charges,nilai_kurs = tran.products.kurs_origin,# type: ignore
        vendor = tran.products.origin_vendor,# type: ignore
        insurance_security_surcharge = price_insurance_security_surcharge,fuel_surcharge = price_fuel_surcharge,
        import_handling_charges = price_import_handling_charges,gst_zero_rated = price_gst_zero_rated,)
    job.save()
    
    job2 = Job(transaksi =tran,tanggal_invoice = tgl_dl,no_invoice = no_invoice_dl,nilai_kurs = tran.products.kurs_destinations,# type: ignore
        vendor = tran.products.destinations_vendor,delivey_to_okusi = price_delivey_to_okusi,delivey_to_betano = price_delivey_to_betano,# type: ignore
        ground_handling = price_ground_handling_dl,forklift_for_heavy_cargo = price_forklift_for_heavy_cargo,
        custom_clearance = price_custom_clearance,delivey_to_hera = price_delivey_to_hera,
        akses_bandara_inspeksi = price_akses_bandara_inspeksi,handling_fee = price_handling_fee,
        admin_fee = admin_fee,fee_collection = fee_collection)
    job2.save()    
   

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_simulasi_form_dua(request, h_ajax, template_name):
    data = dict()
    context = {'h_ajax': h_ajax}
    data['django_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def showparamdua(request):
    jenis_produk = request.GET.get('jenis_produk',None)
    produk = request.GET.get('produk',None)
    tanggal = request.GET.get('tanggal',None)
    poin_satu = request.GET.get('poin_satu',None)
    
    poin_tiga = request.GET.get('poin_tiga',None)
    origin_vendor = request.GET.get('origin_vendor',None)
    
    destinations_vendor = request.GET.get('destinations_vendor',None)    
    
    param = ParameterData.objects.get(products=produk,products__point_satu=poin_satu,products__point_tiga=poin_tiga,
        products__origin_vendor=origin_vendor,products__destinations_vendor=destinations_vendor,
        products__status=1,products__jenis_produk=jenis_produk)
    
    prd = param.products.kode_produk
    org_ven = param.products.origin_vendor
    org = param.products.point_satu
    h_ajax ={'tanggal':tanggal,'produk':prd,'param':param.id,'org':org,'org_ven':org_ven,'jmlv':param.products.jumlah_vendor,  # type: ignore
        'lt_ven':param.products.destinations_vendor,'lt':param.products.point_tiga,'js':param.products.jenis_produk}
    return save_simulasi_form_dua(request, h_ajax,'pengajuan/addpengajuan_dua.html')
    