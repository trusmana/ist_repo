from django import forms
from apps.products.models import Produk,ParameterData


    
class FSForm(forms.ModelForm):
    min_airfreight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_min_airfreight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_max_airfreight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    
    min_handling_charges = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_min_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_max_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    
    ##### Biaya Asuransi
    min_insurance_security_surcharge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_insurance_security_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_high_insurance_security_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    ##biaya tambahan bahan bakar
    
    min_fuel_surcharge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_fuel_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_high_fuel_surcharge = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))

    ###Biaya Penanganan Impor
    min_import_handling_charges = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_import_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_high_import_handling_charges = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))

    
    min_gst_zero_rated = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_gst_zero_rated = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    price_high_gst_zero_rated = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t',
        }))
    
    class Meta:
        model = ParameterData
        fields =['min_airfreight','price_min_airfreight' ,'price_max_airfreight',
            'min_handling_charges','price_min_handling_charges','price_max_handling_charges',
            'min_insurance_security_surcharge','price_insurance_security_surcharge',
            'price_high_insurance_security_surcharge','min_fuel_surcharge','price_fuel_surcharge',
            'price_high_fuel_surcharge','min_import_handling_charges','price_import_handling_charges',
            'price_high_import_handling_charges' ,'min_gst_zero_rated','price_gst_zero_rated',
            'price_high_gst_zero_rated' ]

    


class SLForm(forms.ModelForm):
    ##########Khusus Untuk Sholid Logistik
    ####### Biaya Storage
    min_storage_at_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_high_storage_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_storage_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_pjkp2u_sin_dps_at_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_high_pjkp2u_sin_dps_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_pjkp2u_sin_dps_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_storage_mcl_e_0389249_at_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_high_storage_mcl_e_0389249_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_storage_mcl_e_0389249_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_pjkp2u_dps_dil_at_cost = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_pjkp2u_dps_dil_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_high_pjkp2u_dps_dil_at_cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    ######### Biaya Storege

    min_airfreight_charges = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_airfreight_charges = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_high_airfreight_charges = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_overweight_charges_surcharge = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_overweight_charges_surcharge = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))   
    price_high_overweight_charges_surcharge = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_awb_fee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_awb_fee = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_high_awb_fee  = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))

    min_handling_charges_sl = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_handling_charges_sl = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    price_high_handling_charges_sl = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small uang ttip_t',
        'alt':'integer'}))
    
    class Meta:
        model = ParameterData
        fields =['min_storage_at_cost' ,'price_high_storage_at_cost' ,'price_storage_at_cost' ,
            'min_pjkp2u_sin_dps_at_cost','price_high_pjkp2u_sin_dps_at_cost' ,
            'price_pjkp2u_sin_dps_at_cost' ,'min_storage_mcl_e_0389249_at_cost' ,
            'price_high_storage_mcl_e_0389249_at_cost' ,'price_storage_mcl_e_0389249_at_cost' ,
            'min_pjkp2u_dps_dil_at_cost' ,'price_pjkp2u_dps_dil_at_cost' ,
            'price_high_pjkp2u_dps_dil_at_cost','min_airfreight_charges' ,
            'price_airfreight_charges' ,'price_high_airfreight_charges' ,'min_overweight_charges_surcharge' ,
            'price_overweight_charges_surcharge' ,'price_high_overweight_charges_surcharge' ,
            'min_awb_fee' ,'price_awb_fee' ,'price_high_awb_fee' ,'min_handling_charges_sl',
            'price_handling_charges_sl' ,'price_high_handling_charges_sl' ]

class DLForm(forms.ModelForm):
    min_ground_handling_dl = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_ground_handling_dl = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_ground_handling_dl = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_forklift_for_heavy_cargo = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_forklift_for_heavy_cargo = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_forklift_for_heavy_cargo = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_custom_clearance = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_custom_clearance = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_custom_clearance = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_delivey_to_hera = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_delivey_to_hera = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_delivey_to_hera = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_akses_bandara_inspeksi = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_akses_bandara_inspeksi = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_akses_bandara_inspeksi = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_handling_fee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_handling_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_handling_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_admin_fee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    admin_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    admin_high_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_fee_collection = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    fee_collection = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    fee_high_collection = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))

    class Meta:
        model = ParameterData
        fields = ['min_ground_handling_dl','price_ground_handling_dl' ,'price_high_ground_handling_dl' ,
            'min_forklift_for_heavy_cargo' ,'price_forklift_for_heavy_cargo' ,
            'price_high_forklift_for_heavy_cargo','min_custom_clearance' ,'price_custom_clearance' ,
            'price_high_custom_clearance','min_delivey_to_hera','price_delivey_to_hera',
            'price_high_delivey_to_hera' ,'min_akses_bandara_inspeksi' ,'price_akses_bandara_inspeksi',
            'price_high_akses_bandara_inspeksi' ,
            'min_handling_fee' ,'price_handling_fee' ,'price_high_handling_fee' ,
            'min_admin_fee' ,'admin_fee' ,'admin_high_fee' ,'min_fee_collection' ,
            'fee_collection' ,'fee_high_collection' ,
        ]

    
class DHLForm(forms.Form):
    min_express_wordwide_nondoc= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_express_wordwide_nondoc= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_express_wordwide_nondoc= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_fuel_surcharge_dhl= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_fuel_surcharge_dhl= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_fuel_surcharge_dhl=forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_emergency_situation= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_emergency_situation= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_emergency_situation= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))


class WastilaForm(forms.Form):
    min_custom_learance_fee_handling= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_custom_learance_fee_handling= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_custom_learance_fee_handling= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_heavy_weight_surcharge= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_heavy_weight_surcharge= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_heavy_weight_surcharge= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_agent_fee= forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_agent_fee= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_agent_fee= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_delivery = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_delivery= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_delivery= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
class GastiAsihForm(forms.Form):
    min_pcs = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_pcs= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_pcs= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    
    min_weight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_weight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_weight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))                                       
    
    min_paking = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span2',
        'alt':'integer'}),required =False)
    price_paking = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    price_high_paking = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))