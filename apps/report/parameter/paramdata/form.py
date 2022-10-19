from django import forms

from apps.products.models import Kurs,Produk,STATUS,ParameterData

class ParamForm(forms.Form):
    nama_jasa_pengiriman = forms.CharField(label="Jasa Pengiriman", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    alamat =  forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    telepon =  forms.CharField(label="Telepon", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)


class ParamAllForm(forms.ModelForm):
    products = forms.ModelChoiceField(queryset=Produk.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))

    nilai_kurs = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs='1'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))    
    status_param = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    tgl_aktif_param = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    max_airfreight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control transaction',
        'alt':'integer'}),required =False)
    min_airfreight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control transaction',
        'alt':'integer'}),required =False)
    price_airfreight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control transaction',
        'alt':'integer'}),required =False)

    '''
    
    ########## Khusus Untuk Freight Solutions
    ####Pengiriman Udara
    max_airfreight = forms.FloatField(null=True,blank=True)
    min_airfreight = forms.FloatField(null=True,blank=True)
    price_airfreight = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    ###### Biaya pengurusan / oprasional
    max_handling_charges = forms.FloatField(null=True,blank=True)
    min_handling_charges = forms.FloatField(null=True,blank=True)
    price_handling_charges = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    ##### Biaya Asuransi
    max_insurance_security_surcharge = forms.FloatField(null=True,blank=True)
    min_insurance_security_surcharge = forms.FloatField(null=True,blank=True)
    price_insurance_security_surcharge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    ##biaya tambahan bahan bakar
    max_fuel_surcharge = forms.FloatField(null=True,blank=True)
    min_fuel_surcharge = forms.FloatField(null=True,blank=True)
    price_fuel_surcharge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    ###Biaya Penanganan Impor
    max_import_handling_charges = forms.FloatField(null=True,blank=True)
    max_import_handling_charges = forms.FloatField(null=True,blank=True)
    price_import_handling_charges = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    max_gst_zero_rated = forms.FloatField(null=True,blank=True)
    min_gst_zero_rated = forms.FloatField(null=True,blank=True)
    price_gst_zero_rated = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ##########Akhir Khusus Untuk Freight Solutions

    ##########Khusus Untuk Sholid Logistik
    ####### Biaya Storage
    min_storage_at_cost = forms.FloatField(null=True,blank=True)
    min_storage_at_cost = forms.FloatField(null=True,blank=True)
    price_storage_at_cost = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_pjkp2u_sin_dps_at_cost = forms.FloatField(null=True,blank=True)
    max_pjkp2u_sin_dps_at_cost = forms.FloatField(null=True,blank=True)
    price_pjkp2u_sin_dps_at_cost = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_storage_mcl_e_0389249_at_cost = forms.FloatField(null=True,blank=True)
    max_storage_mcl_e_0389249_at_cost = forms.FloatField(null=True,blank=True)
    price_storage_mcl_e_0389249_at_cost = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_pjkp2u_dps_dil_at_cost = forms.FloatField(null=True,blank=True)
    max_pjkp2u_dps_dil_at_cost = forms.FloatField(null=True,blank=True)
    price_pjkp2u_dps_dil_at_cost = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ######### Biaya Storege

    min_airfreight_charges = forms.FloatField(null=True,blank=True)
    max_airfreight_charges = forms.FloatField(null=True,blank=True)
    price_airfreight_charges = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    man_overweight_charges_surcharge = forms.FloatField(null=True,blank=True)
    min_overweight_charges_surcharge = forms.FloatField(null=True,blank=True)   
    price_overweight_charges_surcharge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    max_awb_fee = forms.FloatField(null=True,blank=True)
    min_awb_fee = forms.FloatField(null=True,blank=True)
    price_awb_fee = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    max_handling_charges = forms.FloatField(null=True,blank=True)
    min_handling_charges = forms.FloatField(null=True,blank=True)
    price_handling_charges = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ########## Akhir Khusus Untuk Sholid Logistik

    ############ khusus logistik dili
    min_ground_handling = forms.FloatField(null=True,blank=True)
    max_ground_handling = forms.FloatField(null=True,blank=True)
    price_ground_handling = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_forklift_for_heavy_cargo = forms.FloatField(null=True,blank=True)
    max_forklift_for_heavy_cargo = forms.FloatField(null=True,blank=True)
    price_forklift_for_heavy_cargo = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_custom_clearance = forms.FloatField(null=True,blank=True)
    min_custom_clearance = forms.FloatField(null=True,blank=True)
    price_custom_clearance = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_delivey_to_hera = forms.FloatField(null=True,blank=True)
    max_delivey_to_hera = forms.FloatField(null=True,blank=True)
    price_delivey_to_hera = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_akses_bandara_inspeksi = forms.FloatField(null=True,blank=True)
    max_akses_bandara_inspeksi = forms.FloatField(null=True,blank=True)
    price_akses_bandara_inspeksi = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_handling_fee = forms.FloatField(null=True,blank=True)
    max_handling_fee = forms.FloatField(null=True,blank=True)
    price_handling_fee = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    admin_fee = forms.FloatField(null=True,blank=True)
    admin_fee = forms.FloatField(null=True,blank=True)
    admin_fee = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0) 
    
    fee_collection = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    ############ Akhir khusus logistik dili

    ########## logistik Indah Sinergi Trading
    min_airfreight_import_handling = forms.FloatField(null=True,blank=True)
    max_airfreight_import_handling = forms.FloatField(null=True,blank=True)
    price_airfreight_import_handling = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_cartage_and_warehouse_charge = forms.FloatField(null=True,blank=True)
    max_cartage_and_warehouse_charge = forms.FloatField(null=True,blank=True)
    price_cartage_and_warehouse_charge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_export_handling = forms.FloatField(null=True,blank=True)
    max_export_handling = forms.FloatField(null=True,blank=True)
    price_export_handling = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    airfreight_sin_dps_dil = forms.FloatField(null=True,blank=True)
    airfreight_sin_dps_dil = forms.FloatField(null=True,blank=True)
    airfreight_sin_dps_dil = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_doc_and_clearance = forms.FloatField(null=True,blank=True)
    max_doc_and_clearance = forms.FloatField(null=True,blank=True)
    price_doc_and_clearance = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    
    min_ground_handling = forms.FloatField(null=True,blank=True)
    max_ground_handling = forms.FloatField(null=True,blank=True)
    price_ground_handling = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_warehouse_charge = forms.FloatField(null=True,blank=True)
    max_warehouse_charge = forms.FloatField(null=True,blank=True)
    price_warehouse_charge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_handling_charge = forms.FloatField(null=True,blank=True)
    max_handling_charge = forms.FloatField(null=True,blank=True)
    price_handling_charge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_delivery = forms.FloatField(null=True,blank=True)
    max_delivery = forms.FloatField(null=True,blank=True)
    price_delivery = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_duty_tax = forms.FloatField(null=True,blank=True)
    max_duty_tax = forms.FloatField(null=True,blank=True)
    price_duty_tax = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)

    min_tax_handling_charge = forms.FloatField(null=True,blank=True)
    max_tax_handling_charge = forms.FloatField(null=True,blank=True)
    price_tax_handling_charge = forms.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True,default=0)
    '''

    class Meta:
        model = ParameterData
        fields = ['id','products','nilai_kurs','status_param','tgl_aktif_param','max_airfreight',
            'min_airfreight','price_airfreight']