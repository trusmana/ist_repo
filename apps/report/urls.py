from django.urls import path, re_path
from apps.report  import views as vreport
from apps.report  import view_kurs as vkurs
from apps.report.parameter.produk import views as pviews
from apps.report.parameter.pengiriman import views as jviews
from apps.report.parameter.paramdata import views_param as prviews
from apps.report.parameter.negara import views as nviews
from apps.report.input import views as inviews ####untuk yg 3 vendor
from apps.report.input import views_dua as inviewsdua ####untuk yg 2 vendor
from apps.report.input import views_satu as inviewssatu ####untuk yg 2 vendor
from apps.report.input import view_ajax as hinviews
from apps.report.input import view_ajax_dua as hajaxtwo
from apps.report.input import data_job as djob
from apps.report.input.edit_inputan import views as v_edit
from apps.report.input import view_cetak as ctk_dok 
from apps.report.parameter.sale import views as s_views
from apps.report.input import view_filter as fviews

urlpatterns = [
    ######data sale
    re_path(r'^sale/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', s_views.list_sale.as_view(),name='d-sale'),

    #####  Menu Cetak Invoice
    path('ctk_job_buy/<int:id>',ctk_dok.invoice, name='ctk-job-buy'),##buy
    path('ctk_job/<int:id>',ctk_dok.debit_note, name='ctk-job'),##Sale

    ######menu Edit Pekerjaan
    path('e_jual/<int:id>',v_edit.edit_jual,name='e-jual'),
    ###################Data Job
    path('d_job_done/',djob.datajob_done, name='d-job-done'),
    path('d_job/',djob.datajob, name='d-job'),
    ####Update Status Pekerjaan
    path('up_date/<int:pk>/',djob.update_job, name='up-job'),
    path('dtl_job/<int:pk>/',djob.detail_job, name='dtl-job'),
    path('dtl_all_job/<int:pk>/',djob.detail_job_all, name='dtl-all-job'),
    ###################Data Job

    ####show kurs
    re_path(r'^kurs/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', vkurs.list_kurs.as_view(),name='d-kurs'),
    path('kurs_add/',vkurs.addkurs,name='add-kurs'),

    ####show produk
    re_path(r'^produk/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', pviews.list_product.as_view(),name='d-produk'),
    ###Add Produk
    path('add_produk/',pviews.addproduk,name='add-produk'),
    ####show Jasa Pengiriman
    re_path(r'^pengiriman/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', jviews.list_pengiriman.as_view(),name='d-pengiriman'),
    ####Add Jasa Pengiriman
    path('add_pengiriman/',jviews.addpengiriman,name='add-pengiriman'),

    ####show Negara
    re_path(r'^negara/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', nviews.list_negara.as_view(),name='d-negara'),
    ####Add Negara
    path('add_negara/',nviews.addnegara,name='add-negara'),

    ####Parameter Data
    re_path(r'^param_data/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', prviews.list_param.as_view(),name='d-param'),
    path('list_param/<int:id>/',prviews.detailparam, name='dtl-param'),
    path('add_paramdata/',prviews.addparam, name='add-paramdata'),
    ####Parameter Data

    ###################Input Pengajuan
    #### Filter Data Pengajuan Berdasarkan Vendor
    path('f_pengajuan/',fviews.filter_pengajuan, name='f-pengajuan'),
    path('in_pengajuan/',fviews.input_pengajuan, name='in-pengajuan'),
    path('in_pengajuan_satu/<int:jv>/',fviews.input_pengajuan_satu, name='in-pengajuan-satu'),
    path('in_pengajuan_dua/',fviews.input_pengajuan_dua, name='in-pengajuan-dua'),
    #### Filter Data Pengajuan 
    path('show_pa/',inviews.showparam,name='show-param'),###tiga vendor
    path('proses_input/<int:param>/',inviews.proses_input,name='proses-input'),###proses  input 3 vendor
    path('show_pa_dua/',inviewsdua.showparamdua,name='show-param-dua'),###dua vendor
    path('proses_input_dua/<int:param>/',inviewsdua.proses_input_dua,name='proses-input-dua'),
    path('show_pa_satu/',inviewssatu.showparamsatu,name='show-param-satu'),###satu vendor
    path('proses_input_satu/<int:param>/',inviewssatu.proses_input_satu,name='proses-input-satu'),
    
    ###################Akhir Input Pengajuan

    ######Fungsi Ajax Hitungan Pembelian
    path('h_airfreight/',hinviews.airfreight, name='h-airfreight'),
    path('h_handling_charges/',hinviews.handling_charges, name='h-handlingcharges'),
    path('h_insurance_security/',hinviews.insurance_security, name='h-insurancesecurity'),
    path('h_fuel_surcharge/',hinviews.fuel_surcharge, name='h-fuelsurcharge'),
    path('h_import_handling_charges/',hinviews.import_handling_charges, name='h-importhandlingcharges'),
    path('h_gst_zero_rated/',hinviews.gst_zero_rated, name='h-gstzerorated'),
    #####Sholid Logistik
    path('h_currency_storage_at_cost/',hinviews.currency_storage_at_cost, name='h-pricestorageatcost'),
    path('h_pjkp2u_sin_dps_at_cost/',hinviews.pjkp2u_sin_dps_at_cost, name='h-pjkp2usindpsatcost'),
    path('h_storage_mcl_e_0389249_at_cost/',hinviews.storage_mcl_e_0389249_at_cost, name='h-storagemcle0389249atcost'),
    path('h_pjkp2u_dps_dil_at_cost/',hinviews.pjkp2u_dps_dil_at_cost, name='h-pjkp2udpsdilatcost'),
    path('h_currency_airfreight_charges/',hinviews.airfreight_charges, name='h-currencyairfreightcharges'),
    path('h_currency_overweight_charges_surcharge/',hinviews.currency_overweight_charges_surcharge, name='h-currencyoverweightchargessurcharg'),
    path('h_cek_currency_awb_fee/',hinviews.cek_currency_awb_fee, name='h-currencyawbfee'),
    path('h_currency_handling_charges/',hinviews.currency_handling_charges, name='h-currencyhandlingcharges'),
    #####DILI
    path('h_currency_ground_handling/',hinviews.currency_ground_handling, name='h-currencygroundhandling'),
    path('h_currency_forklift_for_heavy_cargo/',hinviews.currency_forklift_for_heavy_cargo, name='h-currencyforkliftforheavycargo'),
    path('h_currency_custom_clearance/',hinviews.currency_custom_clearance, name='h-currencycustomclearance'),
    path('h_currency_delivey_to_hera/',hinviews.currency_delivey_to_hera, name='h-currencydeliveytohera'),
    path('h_currency_akses_bandara_inspeksi/',hinviews.currency_akses_bandara_inspeksi, name='h-currencyaksesbandarainspeksi'),
    path('h_currency_handling_fee/',hinviews.currency_handling_fee, name='h-currencyhandlingfee'),
    path('h_currency_admin_fee/',hinviews.currency_admin_fee, name='h-currencyadminfee'),
    path('h_currency_fee_collection/',hinviews.currency_fee_collection, name='h-currencyfeecollection'),

    #########Fungsi AJAX Penjualan
    path('h-salecartage/',hajaxtwo.cartage_warehouse_charge_one, name='h-salecartage'),
    path('h-salecartagetwo/',hajaxtwo.cartage_warehouse_charge_two, name='h-salecartagetwo'),
    path('h-ground_handling_sale/',hajaxtwo.ground_handling_sale, name='h-groundhandlingsale'),
    path('h-warehouse_charge_sale/',hajaxtwo.warehouse_charge_sale, name='h-warehousechargesale'),
    path('h-handling_charge_sale/',hajaxtwo.handling_charge_sale, name='h-handlingchargesale'),
    path('h-delivery_sale/',hajaxtwo.delivery_sale, name='h-deliverysale'),
    path('h-freight_sale/',hajaxtwo.freight_sale, name='h-freightsale'),

]
