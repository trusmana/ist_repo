from django import forms

from apps.products.models import JENISPRODUK, STATUS_UPDATE, Commodity, \
    JasaPengiriman, Negara, ParameterData, ParameterDataBl, Produk,JUMLAH_VENDOR,STATUS_DUTY,\
    DELIVERY_TIMOR_LESTE,STATUS_SHIPMENT

class JvendorForm(forms.Form):
    jvendor = forms.ChoiceField(choices=JUMLAH_VENDOR)
    
    
class PengajuanForm(forms.Form):
    tanggal = forms.DateField(label="Tanggal", widget=forms.DateInput(
        attrs={'class': 'form-control ','readonly':True}))
    jenis_produk = forms.ChoiceField(label='Jenis Pengiriman',widget = forms.Select(attrs={'class':'form-control chosen-select'}),
        choices = JENISPRODUK)    
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status='1',jumlah_vendor = 3),
        widget=forms.Select(attrs={'class':'form-control chosen-select span5'}))
    poin_satu = forms.ModelChoiceField(label="Origin",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    origin_vendor = forms.ModelChoiceField(label="Vendor Origin",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    poin_dua = forms.ModelChoiceField(label="Through",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    through_vendor = forms.ModelChoiceField(label="Vendor Through",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    poin_tiga = forms.ModelChoiceField(label="Destinations",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    destinations_vendor = forms.ModelChoiceField(label="Vendor Destinations",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))

class PengajuanSatuForm(forms.Form):
    tanggal = forms.DateField(label="Tanggal", widget=forms.DateInput(
        attrs={'class': 'form-control ','readonly':True}))
    jenis_produk = forms.ChoiceField(label='Jenis Pengiriman',widget = forms.Select(attrs={'class':'form-control chosen-select'}),
        choices = JENISPRODUK)    
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status=1,jumlah_vendor =1),
        widget=forms.Select(attrs={'class':'form-control chosen-select span5'}))
    poin_tiga = forms.ModelChoiceField(label="Destinations",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    destinations_vendor = forms.ModelChoiceField(label="Vendor Destinations",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))

class PengajuanDuaForm(forms.Form):
    tanggal = forms.DateField(label="Tanggal", widget=forms.DateInput(
        attrs={'class': 'form-control ','readonly':True}))
    jenis_produk = forms.ChoiceField(label='Jenis Pengiriman',widget = forms.Select(attrs={'class':'form-control chosen-select'}),
        choices = JENISPRODUK)    
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status='1',jumlah_vendor =2),
        widget=forms.Select(attrs={'class':'form-control chosen-select span5'}))
    poin_satu = forms.ModelChoiceField(label="Origin",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    origin_vendor = forms.ModelChoiceField(label="Vendor Origin",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    poin_tiga = forms.ModelChoiceField(label="Destinations",queryset=Negara.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    destinations_vendor = forms.ModelChoiceField(label="Vendor Destinations",queryset=JasaPengiriman.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))


class UpdateForm(forms.Form):
    tanggal= forms.DateField(label="Tanggal", widget=forms.DateInput(
        attrs={'class': 'span10 ','readonly':True}))
    status = forms.ChoiceField(choices=STATUS_UPDATE)


##########Akhir Khusus Untuk Freight Solutions
class FSForm(forms.Form):
    tgl_fs = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))

    no_invoice_fs = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    qt_fs = forms.IntegerField(label='Quantity',widget=forms.TextInput(attrs={'class':'input-small',
        'alt':'integer','placeholder':'QTY'}))
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))
    commodity = forms.ModelChoiceField(queryset=Commodity.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control '}))
    param = forms.ModelChoiceField(queryset=ParameterData.objects.filter(status_param='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))    

    weight_fs = forms.DecimalField(label='Weight',widget=forms.TextInput(attrs={
        'class':'uang input-small','onkeyup':'cek_nilai();cek_nilai_handling();cek_insurance_security()\
        ;cek_fuel_surcharge();cek_import_handling_charges();cek_gst_zero_rated()'}))
    
    price_airfreight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    
    ###### Biaya pengurusan / oprasional
    price_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small',
        }))
    ##### Biaya Asuransi
    price_insurance_security_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small',
        }))
    ##biaya tambahan bahan bakar    
    price_fuel_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    ###Biaya Penanganan Impor    
    price_import_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))   
    price_gst_zero_rated = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))

    

class SLForm(forms.Form):
    tgl_sl = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))

    no_invoice_sl = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    no_invoice_sl_2 = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'alt':'integer','placeholder':'No Invoice Dua'}))
    no_invoice_sl_3 = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'alt':'integer','placeholder':'No Invoice Tiga'}))   


    weight_sl = forms.DecimalField(label='Weight',widget=forms.TextInput(attrs={
        'class':'uang input-small','onkeyup':'cek_price_storage_at_cost();cek_pjkp2u_sin_dps_at_cost();\
        cek_storage_mcl_e_0389249_at_cost();cek_pjkp2u_dps_dil_at_cost();cek_airfreight_charges();\
        cek_currency_overweight_charges_surcharg();cek_currency_awb_fee();cek_currency_handling_charges()'}))

    price_storage_at_cost = forms.IntegerField(label = 'Storage At Cost',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    price_pjkp2u_sin_dps_at_cost = forms.IntegerField(label= 'Handling IN',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    price_storage_mcl_e_0389249_at_cost = forms.IntegerField(label= 'PJKP2U',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    price_pjkp2u_dps_dil_at_cost = forms.IntegerField(label='Handling Out',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    ######### Biaya Storege
    price_airfreight_charges = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    ###didiyeu
    price_overweight_charges_surcharge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    price_awb_fee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    price_handling_charges_sl = forms.IntegerField(label= 'Transhipment Handling',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))

class DLForm(forms.Form):
    ############ khusus logistik dili
    tgl_dl = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))

    no_invoice_dl = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    
    weight_dl = forms.DecimalField(label='Weight',widget=forms.TextInput(attrs={
        'class':'input-small','onkeyup':'cek_currency_ground_handling();cek_currency_forklift_for_heavy_cargo();\
        cek_currency_custom_clearance();cek_currency_akses_bandara_inspeksi();cek_currency_delivey_to_hera();\
        cek_currency_handling_fee();cek_currency_admin_fee();cek_currency_fee_collection()'}))    
    price_ground_handling_dl = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    price_forklift_for_heavy_cargo = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    price_custom_clearance = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))

    delivey_to = forms.ChoiceField(widget=forms.Select(attrs={'class':'input-small'}),choices=DELIVERY_TIMOR_LESTE)
    price_delivey_to_hera = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small',})
        ,required=False)
    price_delivey_to_okusi = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small','hidden':'hidden'})
        ,required=False)
    price_delivey_to_betano = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small','hidden':'hidden'})
        ,required=False)
    
    price_akses_bandara_inspeksi = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    price_handling_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    admin_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    fee_collection = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small '}))
    ############ Akhir khusus logistik dili

class SALEForm(forms.Form):
    tanggal = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))    
    etd = forms.DateField(label="ETD", widget=forms.DateInput(
        attrs={'class': 'form-control input-small','placeholder':'DD-MM-YYYY'}))
    eta = forms.DateField(label="ETA", widget=forms.DateInput(
        attrs={'class': 'form-control input-small','placeholder':'DD-MM-YYYY'}))
    
    awb = forms.CharField(label="AWB",widget=forms.TextInput(attrs={'class':'input-small','placeholder':'AWB'}))

    paramsale = forms.ModelChoiceField(queryset=ParameterDataBl.objects.filter(status_param='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))
    
    total_shipment = forms.ChoiceField(label='Total Shipment',widget = forms.Select(attrs={'class':'form-control input-small'}),
        choices = STATUS_SHIPMENT)

    re_export_shipment_one = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    re_export_shipment_one_pcs = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}))
    re_export_shipment_one_qty = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege();'}))

    cartage_warehouse_charge_one = forms.DecimalField(label='1.Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    
    price_cartage_warehouse_charge_one = forms.DecimalField(label='1.Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege();'}))

    
    airfreight_one = forms.DecimalField(label='1.Airfreight Import Handling bda',
        widget=forms.NumberInput(attrs={'class':'input-small '}))
    

    re_export_shipment_two = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    re_export_shipment_two_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}))
    re_export_shipment_two_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_two();'}))    
    cartage_warehouse_charge_two = forms.DecimalField(label='2.Cartage And Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    price_cartage_warehouse_charge_two = forms.DecimalField(label='2.Price Cartage And Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_two();'}))

    
    airfreight_two = forms.DecimalField(label='2.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'h_ground_handling_sale();\
        h_warehouse_charge_sale();h_handling_charge_sale();h_delivery_sale();h_freight_sale()'}))

    ####3
    re_export_shipment_tree = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_tree_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_tree_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_tree();'}),required=False)

    cartage_warehouse_charge_tree = forms.DecimalField(label='3.Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_tree = forms.DecimalField(label='3.Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_tree();'}),required=False)
    
    airfreight_tree = forms.DecimalField(label='3.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####4
    re_export_shipment_four = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_four_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_four_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)

    cartage_warehouse_charge_four = forms.DecimalField(label='4.Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    
    price_cartage_warehouse_charge_four = forms.DecimalField(label='4.Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    
    airfreight_four = forms.DecimalField(label='4.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####4    

    export_handling_sale = forms.DecimalField(label="Export Handling",widget=forms.NumberInput(attrs={'class':'input-small'}))
    freight_sale = forms.DecimalField(label='Airfreight Charge',widget=forms.NumberInput(attrs={'class':'input-small'}))
    price_freight_sale = forms.DecimalField(label='Price AirFreight',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'hitung_freight_sale()'}))

    doc_clearance_sale = forms.DecimalField(label='Doc Clearance',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    price_doc_clearance_sale = forms.DecimalField(label='Price Doc Clearance',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    ground_handling_sale = forms.DecimalField(label='Ground Handling',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    price_ground_handling_sale = forms.DecimalField(label='Price Ground Handling',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'hitung_ground();' }))
    warehouse_charge_sale = forms.DecimalField(label='Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    warehouse_charge_days = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    price_warehouse_charge_sale = forms.DecimalField(label='Price Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'hitung_warehouse_charge_sale()'}))
    handling_charge_sale = forms.DecimalField(label='Handling Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    price_handling_charge_sale = forms.DecimalField(label='Price Handling Charge',
        widget=forms.NumberInput(attrs={'class':'input-small ','onkeyup':'hitung_handling_charge_sale()'}))
    price_delivery_sale = forms.DecimalField(label='Price Delivery',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'hitung_delivery_sale()'}))
    delivery_sale = forms.DecimalField(label='Delivery',
        widget=forms.NumberInput(attrs={'class':'input-small'}))
    status_duty = forms.ChoiceField(label='Status Duty',widget = forms.Select(attrs={'class':'form-control'}),
        choices = STATUS_DUTY)
    duty_tax_sale = forms.DecimalField(label='Duty Tax',widget=forms.NumberInput(attrs={'class':'input-small',
        'onkeyup':'duty_persen()'}),required=False) 
    tax_handling_charge_sale = forms.DecimalField(label='Tax Handling Charge', widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    shipment_value = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    insurance = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)

class TransaksiForm(forms.Form):
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))
    commodity = forms.ModelChoiceField(queryset=Commodity.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control '}))
    param = forms.ModelChoiceField(queryset=ParameterData.objects.filter(status_param='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))    
    qt_fs = forms.IntegerField(label='Quantity',widget=forms.NumberInput(attrs={'class':'input-small',
        'alt':'integer','placeholder':'QTY'}))
    weight_fs = forms.DecimalField(label='Weight',widget=forms.NumberInput(attrs={
        'class':'uang input-small','onkeyup':'cek_amount_gst()','placeholder':'Weight'}))


class GastiAsihForm(forms.Form):
    tgl_ga = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))

    no_invoice_ga = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    #pcs = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    #weight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    paking = forms.IntegerField(label='Handling',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer','onkeyup':'cek_amount_gst()'}))
    jenis = forms.ChoiceField(label='Jenis Pengiriman',widget = forms.Select(attrs={'class':'form-control chosen-select','onchange':'cek_amount_gst()'}),
        choices = JENISPRODUK)  
    amount = forms.IntegerField(label='Amount',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    
    transportation_charge = forms.IntegerField(label='Transportation Charge',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    
class LintasNegaraForm(forms.Form):
    tgl_ln = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))
    no_invoice_ln = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    transit_charge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    transportations_charge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))

class AntarLapanForm(forms.Form):
    tgl_al = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))
    no_invoice_al = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    cbm = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    twentyft = forms.IntegerField(label='20FT',widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))###20ft
    blfee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))
    biaya_peb = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input-small uang',
        'alt':'integer'}))

class DHLForm(forms.Form):
    tgl_dhl = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))
    no_invoice_dhl = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    express_wordwide_nondoc = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    fuel_surcharge_dhl = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    emergency_situation = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))

class WarsilaForm(forms.Form):
    tgl_wsl = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))
    no_invoice_wsl = forms.CharField(label='No Invoice',widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'No Invoice'}))
    custom_learance_fee_handling =forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    heavy_weight_surcharge =forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    agent_fee =forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))
    delivery =forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}))