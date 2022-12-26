from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.conf import settings

from apps.products import models as mp
from apps.report.input.jual import forms as fj

@login_required(login_url=settings.LOGIN_URL)
def input_jual_ist(request,id):
    user = request.user
    trans = mp.Transaksi.objects.get(id=id)
    pse = mp.ParameterDataBl.objects.get(products = trans.products)
    if request.method == "POST":
        forms = fj.SALEForm(request.POST)
        if forms.is_valid():
            paramsale = forms.cleaned_data['paramsale']
            total_shipment = forms.cleaned_data['total_shipment']
            jenis_form = forms.cleaned_data['jenis_form']
            eta = forms.cleaned_data['eta']
            etd = forms.cleaned_data['etd']
            awb = forms.cleaned_data['awb']

            head_address = forms.cleaned_data['head_address']
            consigne = forms.cleaned_data['consigne']
            shipper = forms.cleaned_data['shipper']

            term = forms.cleaned_data['term']
            ddp = forms.cleaned_data['ddp']
            pic = forms.cleaned_data['pic']

            ####akhir Menu Form Input
            repecking = forms.cleaned_data['repecking']
            repecking_price = forms.cleaned_data['repecking_price']
            repecking_qty = forms.cleaned_data['repecking_qty']
            pickup = forms.cleaned_data['pickup']
            pickup_qty = forms.cleaned_data['pickup_qty']
            freight_cost = forms.cleaned_data['freight_cost']
            freight_cost_price = forms.cleaned_data['freight_cost_price']
            freight_cost_qty = forms.cleaned_data['freight_cost_qty']
            overweight_charge = forms.cleaned_data['overweight_charge']
            overweight_charge_price = forms.cleaned_data['overweight_charge_price']
            overweight_charge_qty = forms.cleaned_data['overweight_charge_qty']
            insuranse_forms = forms.cleaned_data['insuranse_forms']
            insuranse_pers = forms.cleaned_data['insuranse_pers']
            insuranse_nilai = forms.cleaned_data['insuranse_nilai']
            gross_weight = forms.cleaned_data['gross_weight']
            nb_of_parcels = forms.cleaned_data['nb_of_parcels']

            re_export_shipment_satu = forms.cleaned_data['re_export_shipment_satu']
            re_export_shipment_satu_pcs = forms.cleaned_data['re_export_shipment_satu_pcs']
            re_export_shipment_satu_qty = forms.cleaned_data['re_export_shipment_satu_qty']

            re_export_shipment_dua = forms.cleaned_data['re_export_shipment_dua']
            re_export_shipment_dua_pcs = forms.cleaned_data['re_export_shipment_dua_pcs']
            re_export_shipment_dua_qty = forms.cleaned_data['re_export_shipment_dua_qty']

            re_export_shipment_tiga = forms.cleaned_data['re_export_shipment_tiga']
            re_export_shipment_tiga_pcs = forms.cleaned_data['re_export_shipment_tiga_pcs']
            re_export_shipment_tiga_qty = forms.cleaned_data['re_export_shipment_tiga_qty']

            re_export_shipment_empat = forms.cleaned_data['re_export_shipment_empat']
            re_export_shipment_empat_pcs = forms.cleaned_data['re_export_shipment_empat_pcs']
            re_export_shipment_empat_qty = forms.cleaned_data['re_export_shipment_empat_qty']

            re_export_shipment_lima = forms.cleaned_data['re_export_shipment_lima']
            re_export_shipment_lima_pcs = forms.cleaned_data['re_export_shipment_lima_pcs']
            re_export_shipment_lima_qty = forms.cleaned_data['re_export_shipment_lima_qty']

            re_export_shipment_enam = forms.cleaned_data['re_export_shipment_enam']
            re_export_shipment_enam_pcs = forms.cleaned_data['re_export_shipment_enam_pcs']
            re_export_shipment_enam_qty = forms.cleaned_data['re_export_shipment_enam_qty']

            re_export_shipment_tujuh = forms.cleaned_data['re_export_shipment_tujuh']
            re_export_shipment_tujuh_pcs = forms.cleaned_data['re_export_shipment_tujuh_pcs']
            re_export_shipment_tujuh_qty = forms.cleaned_data['re_export_shipment_tujuh_qty']

            re_export_shipment_delapan = forms.cleaned_data['re_export_shipment_delapan']
            re_export_shipment_delapan_pcs = forms.cleaned_data['re_export_shipment_delapan_pcs']
            re_export_shipment_delapan_qty = forms.cleaned_data['re_export_shipment_delapan_qty']

            re_export_shipment_sembilan = forms.cleaned_data['re_export_shipment_sembilan']
            re_export_shipment_sembilan_pcs = forms.cleaned_data['re_export_shipment_sembilan_pcs']
            re_export_shipment_sembilan_qty = forms.cleaned_data['re_export_shipment_sembilan_qty']

            re_export_shipment_sepuluh = forms.cleaned_data['re_export_shipment_sepuluh']
            re_export_shipment_sepuluh_pcs = forms.cleaned_data['re_export_shipment_sepuluh_pcs']
            re_export_shipment_sepuluh_qty = forms.cleaned_data['re_export_shipment_sepuluh_qty']

            re_export_shipment_sebelas = forms.cleaned_data['re_export_shipment_sebelas']
            re_export_shipment_sebelas_pcs = forms.cleaned_data['re_export_shipment_sebelas_pcs']
            re_export_shipment_sebelas_qty = forms.cleaned_data['re_export_shipment_sebelas_qty']    

            re_export_shipment_duabelas = forms.cleaned_data['re_export_shipment_duabelas']
            re_export_shipment_duabelas_pcs = forms.cleaned_data['re_export_shipment_duabelas_pcs']
            re_export_shipment_duabelas_qty = forms.cleaned_data['re_export_shipment_duabelas_qty']

            re_export_shipment_tigabelas = forms.cleaned_data['re_export_shipment_tigabelas']
            re_export_shipment_tigabelas_pcs = forms.cleaned_data['re_export_shipment_tigabelas_pcs']
            re_export_shipment_tigabelas_qty = forms.cleaned_data['re_export_shipment_tigabelas_qty']

            re_export_shipment_empatbelas = forms.cleaned_data['re_export_shipment_empatbelas']
            re_export_shipment_empatbelas_pcs = forms.cleaned_data['re_export_shipment_empatbelas_pcs']
            re_export_shipment_empatbelas_qty = forms.cleaned_data['re_export_shipment_empatbelas_qty']

            re_export_shipment_limabelas = forms.cleaned_data['re_export_shipment_limabelas']
            re_export_shipment_limabelas_pcs = forms.cleaned_data['re_export_shipment_limabelas_pcs']
            re_export_shipment_limabelas_qty = forms.cleaned_data['re_export_shipment_limabelas_qty']

            re_export_shipment_enambelas = forms.cleaned_data['re_export_shipment_enambelas']
            re_export_shipment_enambelas_pcs = forms.cleaned_data['re_export_shipment_enambelas_pcs']
            re_export_shipment_enambelas_qty = forms.cleaned_data['re_export_shipment_enambelas_qty']

            re_export_shipment_tujuhbelas = forms.cleaned_data['re_export_shipment_tujuhbelas']
            re_export_shipment_tujuhbelas_pcs = forms.cleaned_data['re_export_shipment_tujuhbelas_pcs']
            re_export_shipment_tujuhbelas_qty = forms.cleaned_data['re_export_shipment_tujuhbelas_qty']

            re_export_shipment_delapanbelas = forms.cleaned_data['re_export_shipment_delapanbelas']
            re_export_shipment_delapanbelas_pcs = forms.cleaned_data['re_export_shipment_delapanbelas_pcs']
            re_export_shipment_delapanbelas_qty = forms.cleaned_data['re_export_shipment_delapanbelas_qty']

            re_export_shipment_sembilanbelas = forms.cleaned_data['re_export_shipment_sembilanbelas']
            re_export_shipment_sembilanbelas_pcs = forms.cleaned_data['re_export_shipment_sembilanbelas_pcs']
            re_export_shipment_sembilanbelas_qty = forms.cleaned_data['re_export_shipment_sembilanbelas_qty']

            re_export_shipment_duapuluh = forms.cleaned_data['re_export_shipment_duapuluh']
            re_export_shipment_duapuluh_pcs = forms.cleaned_data['re_export_shipment_duapuluh_pcs']
            re_export_shipment_duapuluh_qty = forms.cleaned_data['re_export_shipment_duapuluh_qty']

            price_cartage_warehouse_charge_satu =forms.cleaned_data['price_cartage_warehouse_charge_satu']
            price_cartage_warehouse_charge_dua =forms.cleaned_data['price_cartage_warehouse_charge_dua']
            price_cartage_warehouse_charge_tiga =forms.cleaned_data['price_cartage_warehouse_charge_tiga']
            price_cartage_warehouse_charge_empat =forms.cleaned_data['price_cartage_warehouse_charge_empat']
            price_cartage_warehouse_charge_lima =forms.cleaned_data['price_cartage_warehouse_charge_lima']
            price_cartage_warehouse_charge_enam =forms.cleaned_data['price_cartage_warehouse_charge_enam']
            price_cartage_warehouse_charge_tujuh =forms.cleaned_data['price_cartage_warehouse_charge_tujuh']
            price_cartage_warehouse_charge_delapan =forms.cleaned_data['price_cartage_warehouse_charge_delapan']
            price_cartage_warehouse_charge_sembilan =forms.cleaned_data['price_cartage_warehouse_charge_sembilan']
            price_cartage_warehouse_charge_sepuluh =forms.cleaned_data['price_cartage_warehouse_charge_sepuluh']
            price_cartage_warehouse_charge_sebelas =forms.cleaned_data['price_cartage_warehouse_charge_sebelas']
            price_cartage_warehouse_charge_duabelas =forms.cleaned_data['price_cartage_warehouse_charge_duabelas']
            price_cartage_warehouse_charge_tigabelas=forms.cleaned_data['price_cartage_warehouse_charge_tigabelas']
            price_cartage_warehouse_charge_limabelas =forms.cleaned_data['price_cartage_warehouse_charge_limabelas']
            price_cartage_warehouse_charge_tujuhbelas =forms.cleaned_data['price_cartage_warehouse_charge_tujuhbelas']
            price_cartage_warehouse_charge_delapanbelas =forms.cleaned_data['price_cartage_warehouse_charge_delapanbelas']
            price_cartage_warehouse_charge_sembilanbelas =forms.cleaned_data['price_cartage_warehouse_charge_sembilanbelas']
            price_cartage_warehouse_charge_daupuluh =forms.cleaned_data['price_cartage_warehouse_charge_daupuluh']
            
            cartage_warehouse_charge_satu = forms.cleaned_data['cartage_warehouse_charge_satu']
            cartage_warehouse_charge_dua = forms.cleaned_data['cartage_warehouse_charge_dua']
            cartage_warehouse_charge_tiga = forms.cleaned_data['cartage_warehouse_charge_tiga']
            cartage_warehouse_charge_empat = forms.cleaned_data['cartage_warehouse_charge_empat']
            cartage_warehouse_charge_lima = forms.cleaned_data['cartage_warehouse_charge_lima']
            cartage_warehouse_charge_enam = forms.cleaned_data['cartage_warehouse_charge_enam']
            cartage_warehouse_charge_tujuh = forms.cleaned_data['cartage_warehouse_charge_tujuh']
            cartage_warehouse_charge_delapan = forms.cleaned_data['cartage_warehouse_charge_delapan']
            cartage_warehouse_charge_sembilan = forms.cleaned_data['cartage_warehouse_charge_sembilan']
            cartage_warehouse_charge_sepuluh = forms.cleaned_data['cartage_warehouse_charge_sepuluh']
            cartage_warehouse_charge_sebelas = forms.cleaned_data['cartage_warehouse_charge_sebelas']
            cartage_warehouse_charge_duabelas = forms.cleaned_data['cartage_warehouse_charge_duabelas']
            cartage_warehouse_charge_tigabelas = forms.cleaned_data['cartage_warehouse_charge_tigabelas']
            cartage_warehouse_charge_empatbelas = forms.cleaned_data['cartage_warehouse_charge_empatbelas']
            cartage_warehouse_charge_limabelas = forms.cleaned_data['cartage_warehouse_charge_limabelas']
            cartage_warehouse_charge_enambelas = forms.cleaned_data['cartage_warehouse_charge_enambelas']
            cartage_warehouse_charge_tujuhbelas = forms.cleaned_data['cartage_warehouse_charge_tujuhbelas']
            cartage_warehouse_charge_delapanbelas = forms.cleaned_data['cartage_warehouse_charge_delapanbelas']
            cartage_warehouse_charge_sembilanbelas = forms.cleaned_data['cartage_warehouse_charge_sembilanbelas']
            cartage_warehouse_charge_duapuluh = forms.cleaned_data['cartage_warehouse_charge_duapuluh']

            airfreight_satu = forms.cleaned_data['airfreight_satu']
            airfreight_dua = forms.cleaned_data['airfreight_dua']
            airfreight_tiga = forms.cleaned_data['airfreight_tiga']
            airfreight_empat = forms.cleaned_data['airfreight_empat']
            airfreight_lima = forms.cleaned_data['airfreight_lima']
            airfreight_enam = forms.cleaned_data['airfreight_enam']
            airfreight_tujuh = forms.cleaned_data['airfreight_tujuh']
            airfreight_delapan = forms.cleaned_data['airfreight_delapan']
            airfreight_sembilan = forms.cleaned_data['airfreight_sembilan']
            airfreight_sepuluh = forms.cleaned_data['airfreight_sepuluh']
            airfreight_sebelas = forms.cleaned_data['airfreight_sebelas']
            airfreight_duabelas = forms.cleaned_data['airfreight_duabelas']
            airfreight_tigabelas = forms.cleaned_data['airfreight_tigabelas']
            airfreight_empatbelas = forms.cleaned_data['airfreight_empatbelas']
            airfreight_limabelas = forms.cleaned_data['airfreight_limabelas']
            airfreight_enambelas = forms.cleaned_data['airfreight_enambelas']
            airfreight_tujuhbelas = forms.cleaned_data['airfreight_tujuhbelas']
            airfreight_delapanbelas = forms.cleaned_data['airfreight_delapanbelas']
            airfreight_sembilanbelas = forms.cleaned_data['airfreight_sembilanbelas']
            airfreight_duapuluh = forms.cleaned_data['airfreight_duapuluh']
            ####akhir Menu Form Input
                        
            price_doc_clearance_sale = forms.cleaned_data['price_doc_clearance_sale']
            price_ground_handling_sale = forms.cleaned_data['price_ground_handling_sale']
            price_warehouse_charge_sale = forms.cleaned_data['price_warehouse_charge_sale']
            price_handling_charge_sale = forms.cleaned_data['price_handling_charge_sale']
            price_delivery_sale = forms.cleaned_data['price_delivery_sale']
            price_freight_sale = forms.cleaned_data['price_freight_sale']

            export_handling_sale = forms.cleaned_data['export_handling_sale']
            freight_sale = forms.cleaned_data['freight_sale']
            doc_clearance_sale = forms.cleaned_data['doc_clearance_sale']
            ground_handling_sale = forms.cleaned_data['ground_handling_sale']
            warehouse_charge_sale = forms.cleaned_data['warehouse_charge_sale']
            warehouse_charge_days = forms.cleaned_data['warehouse_charge_days']
            handling_charge_sale = forms.cleaned_data['handling_charge_sale']
            delivery_sale = forms.cleaned_data['delivery_sale']
            duty_tax_sale = forms.cleaned_data['duty_tax_sale']
            status_duty = forms.cleaned_data['status_duty']
            tax_handling_charge_sale = forms.cleaned_data['tax_handling_charge_sale']
            shipment_value = forms.cleaned_data['shipment_value']
            insurance = forms.cleaned_data['insurance']

            ms =mp.MenuInputSale(jenis_form=jenis_form,total_shipment=total_shipment,
                re_export_shipment_satu = re_export_shipment_satu,
                re_export_shipment_satu_pcs = re_export_shipment_satu_pcs,
                re_export_shipment_satu_qty = re_export_shipment_satu_qty,

                re_export_shipment_dua = re_export_shipment_dua,
                re_export_shipment_dua_pcs = re_export_shipment_dua_pcs,
                re_export_shipment_dua_qty = re_export_shipment_dua_qty,

                re_export_shipment_tiga = re_export_shipment_tiga,
                re_export_shipment_tiga_pcs = re_export_shipment_tiga_pcs,
                re_export_shipment_tiga_qty = re_export_shipment_tiga_qty,

                re_export_shipment_empat = re_export_shipment_empat,
                re_export_shipment_empat_pcs = re_export_shipment_empat_pcs,
                re_export_shipment_empat_qty = re_export_shipment_empat_qty,

                re_export_shipment_lima = re_export_shipment_lima,
                re_export_shipment_lima_pcs = re_export_shipment_lima_pcs,
                re_export_shipment_lima_qty = re_export_shipment_lima_qty,

                re_export_shipment_enam = re_export_shipment_enam,
                re_export_shipment_enam_pcs = re_export_shipment_enam_pcs,
                re_export_shipment_enam_qty = re_export_shipment_enam_qty,

                re_export_shipment_tujuh = re_export_shipment_tujuh,
                re_export_shipment_tujuh_pcs = re_export_shipment_tujuh_pcs,
                re_export_shipment_tujuh_qty = re_export_shipment_tujuh_qty,

                re_export_shipment_delapan = re_export_shipment_delapan,
                re_export_shipment_delapan_pcs = re_export_shipment_delapan_pcs,
                re_export_shipment_delapan_qty = re_export_shipment_delapan_qty,

                re_export_shipment_sembilan = re_export_shipment_sembilan,
                re_export_shipment_sembilan_pcs = re_export_shipment_sembilan_pcs,
                re_export_shipment_sembilan_qty = re_export_shipment_sembilan_qty,

                re_export_shipment_sepuluh = re_export_shipment_sepuluh,
                re_export_shipment_sepuluh_pcs = re_export_shipment_sepuluh_pcs,
                re_export_shipment_sepuluh_qty = re_export_shipment_sepuluh_qty,

                re_export_shipment_sebelas = re_export_shipment_sebelas,
                re_export_shipment_sebelas_pcs = re_export_shipment_sebelas_pcs,
                re_export_shipment_sebelas_qty = re_export_shipment_sebelas_qty ,

                re_export_shipment_duabelas = re_export_shipment_duabelas,
                re_export_shipment_duabelas_pcs = re_export_shipment_duabelas_pcs,
                re_export_shipment_duabelas_qty = re_export_shipment_duabelas_qty,

                re_export_shipment_tigabelas = re_export_shipment_tigabelas,
                re_export_shipment_tigabelas_pcs = re_export_shipment_tigabelas_pcs,
                re_export_shipment_tigabelas_qty = re_export_shipment_tigabelas_qty,

                re_export_shipment_empatbelas = re_export_shipment_empatbelas,
                re_export_shipment_empatbelas_pcs = re_export_shipment_empatbelas_pcs,
                re_export_shipment_empatbelas_qty = re_export_shipment_empatbelas_qty,

                re_export_shipment_limabelas = re_export_shipment_limabelas,
                re_export_shipment_limabelas_pcs = re_export_shipment_limabelas_pcs,
                re_export_shipment_limabelas_qty = re_export_shipment_limabelas_qty,

                re_export_shipment_enambelas = re_export_shipment_enambelas,
                re_export_shipment_enambelas_pcs = re_export_shipment_enambelas_pcs,
                re_export_shipment_enambelas_qty = re_export_shipment_enambelas_qty,

                re_export_shipment_tujuhbelas = re_export_shipment_tujuhbelas,
                re_export_shipment_tujuhbelas_pcs = re_export_shipment_tujuhbelas_pcs,
                re_export_shipment_tujuhbelas_qty = re_export_shipment_tujuhbelas_qty,

                re_export_shipment_delapanbelas = re_export_shipment_delapanbelas,
                re_export_shipment_delapanbelas_pcs = re_export_shipment_delapanbelas_pcs,
                re_export_shipment_delapanbelas_qty = re_export_shipment_delapanbelas_qty,

                re_export_shipment_sembilanbelas = re_export_shipment_sembilanbelas,
                re_export_shipment_sembilanbelas_pcs = re_export_shipment_sembilanbelas_pcs,
                re_export_shipment_sembilanbelas_qty = re_export_shipment_sembilanbelas_qty,

                re_export_shipment_duapuluh = re_export_shipment_duapuluh,
                re_export_shipment_duapuluh_pcs = re_export_shipment_duapuluh_pcs,
                re_export_shipment_duapuluh_qty = re_export_shipment_duapuluh_qty,

                price_cartage_warehouse_charge_satu = price_cartage_warehouse_charge_satu,
                price_cartage_warehouse_charge_dua = price_cartage_warehouse_charge_dua,
                price_cartage_warehouse_charge_tiga = price_cartage_warehouse_charge_tiga,
                price_cartage_warehouse_charge_empat = price_cartage_warehouse_charge_empat,
                price_cartage_warehouse_charge_lima = price_cartage_warehouse_charge_lima,
                price_cartage_warehouse_charge_enam = price_cartage_warehouse_charge_enam,
                price_cartage_warehouse_charge_tujuh = price_cartage_warehouse_charge_tujuh,
                price_cartage_warehouse_charge_delapan = price_cartage_warehouse_charge_delapan,
                price_cartage_warehouse_charge_sembilan = price_cartage_warehouse_charge_sembilan,
                price_cartage_warehouse_charge_sepuluh = price_cartage_warehouse_charge_sepuluh,
                price_cartage_warehouse_charge_sebelas = price_cartage_warehouse_charge_sebelas,
                price_cartage_warehouse_charge_duabelas = price_cartage_warehouse_charge_duabelas,
                price_cartage_warehouse_charge_tigabelas= price_cartage_warehouse_charge_tigabelas,
                price_cartage_warehouse_charge_limabelas = price_cartage_warehouse_charge_limabelas,
                price_cartage_warehouse_charge_tujuhbelas = price_cartage_warehouse_charge_tujuhbelas,
                price_cartage_warehouse_charge_delapanbelas = price_cartage_warehouse_charge_delapanbelas,
                price_cartage_warehouse_charge_sembilanbelas = price_cartage_warehouse_charge_sembilanbelas,
                price_cartage_warehouse_charge_daupuluh = price_cartage_warehouse_charge_daupuluh,

                cartage_warehouse_charge_satu = cartage_warehouse_charge_satu,
                cartage_warehouse_charge_dua = cartage_warehouse_charge_dua,
                cartage_warehouse_charge_tiga = cartage_warehouse_charge_tiga,
                cartage_warehouse_charge_empat = cartage_warehouse_charge_empat,
                cartage_warehouse_charge_lima = cartage_warehouse_charge_lima,
                cartage_warehouse_charge_enam = cartage_warehouse_charge_enam,
                cartage_warehouse_charge_tujuh = cartage_warehouse_charge_tujuh,
                cartage_warehouse_charge_delapan = cartage_warehouse_charge_delapan,
                cartage_warehouse_charge_sembilan = cartage_warehouse_charge_sembilan,
                cartage_warehouse_charge_sepuluh = cartage_warehouse_charge_sepuluh,
                cartage_warehouse_charge_sebelas = cartage_warehouse_charge_sebelas,
                cartage_warehouse_charge_duabelas = cartage_warehouse_charge_duabelas,
                cartage_warehouse_charge_tigabelas = cartage_warehouse_charge_tigabelas,
                cartage_warehouse_charge_empatbelas = cartage_warehouse_charge_empatbelas,
                cartage_warehouse_charge_limabelas = cartage_warehouse_charge_limabelas,
                cartage_warehouse_charge_enambelas = cartage_warehouse_charge_enambelas,
                cartage_warehouse_charge_tujuhbelas = cartage_warehouse_charge_tujuhbelas,
                cartage_warehouse_charge_delapanbelas = cartage_warehouse_charge_delapanbelas,
                cartage_warehouse_charge_sembilanbelas = cartage_warehouse_charge_sembilanbelas,
                cartage_warehouse_charge_duapuluh = cartage_warehouse_charge_duapuluh,

                airfreight_satu = airfreight_satu,
                airfreight_dua = airfreight_dua,
                airfreight_tiga = airfreight_tiga,
                airfreight_empat = airfreight_empat,
                airfreight_lima = airfreight_lima,
                airfreight_enam = airfreight_enam,
                airfreight_tujuh = airfreight_tujuh,
                airfreight_delapan = airfreight_delapan,
                airfreight_sembilan = airfreight_sembilan,
                airfreight_sepuluh = airfreight_sepuluh,
                airfreight_sebelas = airfreight_sebelas,
                airfreight_duabelas = airfreight_duabelas,
                airfreight_tigabelas = airfreight_tigabelas,
                airfreight_empatbelas = airfreight_empatbelas,
                airfreight_limabelas = airfreight_limabelas,
                airfreight_enambelas = airfreight_enambelas,
                airfreight_tujuhbelas = airfreight_tujuhbelas,
                airfreight_delapanbelas = airfreight_delapanbelas,
                airfreight_sembilanbelas = airfreight_sembilanbelas,
                airfreight_duapuluh = airfreight_duapuluh,

                repecking = repecking,repecking_price = repecking_price,repecking_qty = repecking_qty,                
                pickup = pickup,pickup_qty = pickup_qty,nb_of_parcels =nb_of_parcels,gross_weight=gross_weight,
                freight_cost = freight_cost,freight_cost_price = freight_cost_price,freight_cost_qty = freight_cost_qty,
                overweight_charge = overweight_charge,overweight_charge_price = overweight_charge_price,overweight_charge_qty = overweight_charge_qty,
                insuranse_forms = insuranse_forms,insuranse_nilai = insuranse_nilai,insuranse_pers = insuranse_pers)
            ms.save()
            sale = mp.Sale(trans=trans,prod=paramsale,cu=user,formsale=ms,
                head_address = head_address,consigne = consigne,shipper = shipper,
                term = term,ddp = ddp,pic = pic,
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
        forms = fj.SALEForm(initial={'tanggal':datetime.date.today(),'paramsale':pse.id})  # type: ignore
    return render(request,'pengajuan/jual/proses_jual.html',{'sl':forms,'param':pse})  # type: ignore