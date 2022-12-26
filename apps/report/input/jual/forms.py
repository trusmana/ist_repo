from django import forms

from apps.products import models as mp

class SALEForm(forms.Form):
    tanggal = forms.DateField(label="Tanggal Invoice", widget=forms.DateInput(
        attrs={'class': 'form-control '}))    
    etd = forms.DateField(label="ETD", widget=forms.DateInput(
        attrs={'class': 'form-control input-small','placeholder':'DD-MM-YYYY'}))
    eta = forms.DateField(label="ETA", widget=forms.DateInput(
        attrs={'class': 'form-control input-small','placeholder':'DD-MM-YYYY'}))
    awb = forms.CharField(label="AWB",widget=forms.TextInput(attrs={'class':'input-small','placeholder':'AWB'}))
    

    head_address = forms.ModelChoiceField(queryset=mp.AddresInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))
    consigne = forms.ModelChoiceField(queryset=mp.ConsigneInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))
    shipper = forms.ModelChoiceField(queryset=mp.ShipperInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))
    
    term = forms.ModelChoiceField(queryset=mp.TermInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))
    ddp = forms.ModelChoiceField(queryset=mp.DdpInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))
    pic = forms.ModelChoiceField(queryset=mp.PicInvoice.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control'}))

    paramsale = forms.ModelChoiceField(queryset=mp.ParameterDataBl.objects.filter(status_param='1'),
        widget=forms.Select(attrs={'class':'form-control ','readonly':True}))
    
    total_shipment = forms.ChoiceField(label='Total Shipment',widget = forms.Select(attrs={'class':'form-control input-small'}),
        choices = mp.STATUS_SHIPMENT,required=False)
    jenis_form = forms.ChoiceField(label='Jenis Form',widget = forms.Select(attrs={'class':'form-control input-small'}),
        choices = mp.JFORM,required=False)

    nb_of_parcels = forms.DecimalField(label='NB OF Parcels ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    gross_weight = forms.DecimalField(label='Gross Weight ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    repecking = forms.DecimalField(label='Repacking ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    repecking_price = forms.DecimalField(label='Repacking Price',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    repecking_qty = forms.DecimalField(label='Repacking QTY',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    pickup = forms.DecimalField(label='Pickup ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    pickup_qty = forms.DecimalField(label='Pickup QTY',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    freight_cost = forms.DecimalField(label='Freight Cost ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    freight_cost_price = forms.DecimalField(label='Freight Cost Price ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    freight_cost_qty = forms.DecimalField(label='Freight Cost Qty ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    overweight_charge = forms.DecimalField(label='Overweight Charge ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    overweight_charge_price = forms.DecimalField(label='Overweight Charge Price ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    overweight_charge_qty= forms.DecimalField(label='Overweight Charge QTY ',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    insuranse_forms   = forms.DecimalField(label='Insurance Form',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    insuranse_nilai   = forms.DecimalField(label='Insurance Price',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    insuranse_pers   = forms.DecimalField(label='Insurance Persentasi',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    nb_of_parcels = forms.DecimalField(label='NB Of Parcels',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    gross_weight = forms.DecimalField(label='Gross Weight',widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    ####1
    re_export_shipment_satu = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_satu_pcs = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_satu_qty = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY'}),required=False)
    cartage_warehouse_charge_satu = forms.DecimalField(label='1.Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)   
    price_cartage_warehouse_charge_satu = forms.DecimalField(label='1.Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)    
    airfreight_satu = forms.DecimalField(label='1.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####1
    ####2
    re_export_shipment_dua = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_dua_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_dua_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_two();'}),required=False)    
    cartage_warehouse_charge_dua = forms.DecimalField(label='2.Cartage And Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_dua = forms.DecimalField(label='2.Price Cartage And Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_two();'}),required=False)
    airfreight_dua = forms.DecimalField(label='2.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'h_ground_handling_sale();\
        h_warehouse_charge_sale();h_handling_charge_sale();h_delivery_sale();h_freight_sale()'}),required=False)
    ####2
    ####3
    re_export_shipment_tiga = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_tiga_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_tiga_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_tree();'}),required=False)
    cartage_warehouse_charge_tiga = forms.DecimalField(label='3.Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_tiga = forms.DecimalField(label='3.Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_tree();'}),required=False)
    airfreight_tiga = forms.DecimalField(label='3.Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####4
    re_export_shipment_empat = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_empat_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_empat_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_empat = forms.DecimalField(label='4. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_empat = forms.DecimalField(label='4. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_empat = forms.DecimalField(label='4. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####4
    ####5
    re_export_shipment_lima = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_lima_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_lima_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_lima = forms.DecimalField(label='5. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_lima = forms.DecimalField(label='5. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_lima = forms.DecimalField(label='5. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####5
    ####6
    re_export_shipment_enam = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_enam_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_enam_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_enam = forms.DecimalField(label='6. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_enam = forms.DecimalField(label='6. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_enam = forms.DecimalField(label='6. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####6
    ####7
    re_export_shipment_tujuh = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_tujuh_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_tujuh_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_tujuh = forms.DecimalField(label='7. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_tujuh = forms.DecimalField(label='7. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_tujuh = forms.DecimalField(label='7. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####7
    ####8
    re_export_shipment_delapan = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_delapan_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_delapan_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_delapan = forms.DecimalField(label='8. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_delapan = forms.DecimalField(label='8. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_delapan = forms.DecimalField(label='8. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####8
    ####9
    re_export_shipment_sembilan = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_sembilan_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_sembilan_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_sembilan = forms.DecimalField(label='9. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_sembilan = forms.DecimalField(label='9. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_sembilan = forms.DecimalField(label='9. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####9
    ####10
    re_export_shipment_sepuluh = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_sepuluh_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_sepuluh_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_sepuluh = forms.DecimalField(label='10. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_sepuluh = forms.DecimalField(label='10. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_sepuluh = forms.DecimalField(label='10. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####10
    ####11
    re_export_shipment_sebelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_sebelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_sebelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_sebelas = forms.DecimalField(label='11. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_sebelas = forms.DecimalField(label='11. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_sebelas = forms.DecimalField(label='11. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####11
    ####12
    re_export_shipment_duabelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_duabelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_duabelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_duabelas = forms.DecimalField(label='12. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_duabelas = forms.DecimalField(label='12. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_duabelas = forms.DecimalField(label='12. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####12
    ####13
    re_export_shipment_tigabelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_tigabelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_tigabelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_tigabelas = forms.DecimalField(label='13. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_tigabelas = forms.DecimalField(label='13. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_tigabelas = forms.DecimalField(label='13. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####13
    ####14
    re_export_shipment_empatbelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_empatbelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_empatbelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_empatbelas = forms.DecimalField(label='14. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_empatbelas = forms.DecimalField(label='14. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_empatbelas = forms.DecimalField(label='14. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####14 
    ####15
    re_export_shipment_limabelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_limabelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_limabelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_limabelas = forms.DecimalField(label='15. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_limabelas = forms.DecimalField(label='15. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_limabelas = forms.DecimalField(label='15. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####15
    ####16
    re_export_shipment_enambelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_enambelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_enambelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_enambelas = forms.DecimalField(label='16. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_enambelas = forms.DecimalField(label='16. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_enambelas = forms.DecimalField(label='16. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####16
    ####17
    re_export_shipment_tujuhbelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_tujuhbelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_tujuhbelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_tujuhbelas = forms.DecimalField(label='17. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_tujuhbelas = forms.DecimalField(label='17. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_tujuhbelas = forms.DecimalField(label='17. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####17
    ####18
    re_export_shipment_delapanbelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_delapanbelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_delapanbelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_delapanbelas = forms.DecimalField(label='18. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_delapanbelas = forms.DecimalField(label='18. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_delapanbelas = forms.DecimalField(label='18. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####18
    ####19
    re_export_shipment_sembilanbelas = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_sembilanbelas_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_sembilanbelas_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_sembilanbelas = forms.DecimalField(label='19. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_sembilanbelas = forms.DecimalField(label='19. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_sembilanbelas = forms.DecimalField(label='19. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####19   
    ####20
    re_export_shipment_duapuluh = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}),required=False)
    re_export_shipment_duapuluh_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'PCS'}),required=False)
    re_export_shipment_duapuluh_qty = forms.DecimalField(initial=0,widget=forms.TextInput(attrs={'class':'input-small',
        'placeholder':'QTY','onkeyup':'sale_cartege_four();'}),required=False)
    cartage_warehouse_charge_duapuluh = forms.DecimalField(label='20. Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    price_cartage_warehouse_charge_daupuluh = forms.DecimalField(label='20. Price Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'sale_cartege_four();'}),required=False)
    airfreight_duapuluh = forms.DecimalField(label='20. Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small '}),required=False)
    ####20

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
        choices = mp.STATUS_DUTY)
    duty_tax_sale = forms.DecimalField(label='Duty Tax',widget=forms.NumberInput(attrs={'class':'input-small',
        'onkeyup':'duty_persen()'}),required=False) 
    tax_handling_charge_sale = forms.DecimalField(label='Tax Handling Charge', widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    shipment_value = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
    insurance = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small'}),required=False)
