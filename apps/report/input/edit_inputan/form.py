from django import forms

from apps.products.models import ParameterDataBl, Sale

class JualForm(forms.ModelForm):
   
    cartage_warehouse_charge_one = forms.DecimalField(label='Cartage and Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    
    airfreight_one = forms.DecimalField(label='Airfreight Import Handling bda',
        widget=forms.NumberInput(attrs={'class':'input-small  ttip_t'}))
    

    re_export_shipment_two = forms.CharField(widget=forms.TextInput(attrs={'class':'input-small'}))
    re_export_shipment_two_pcs = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small ttip_t',
        'placeholder':'PCS'}))
    re_export_shipment_two_qty = forms.DecimalField(widget=forms.TextInput(attrs={'class':'input-small ttip_t',
        'placeholder':'QTY','onkeyup':'sale_cartege_two();'}))    
    cartage_warehouse_charge_two = forms.DecimalField(label='Cartage And Warehouse Charge',
        widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    
    airfreight_two = forms.DecimalField(label='Airfreight Import Handling ',
        widget=forms.NumberInput(attrs={'class':'input-small','onkeyup':'h_ground_handling_sale();\
        h_warehouse_charge_sale();h_handling_charge_sale();h_delivery_sale();h_freight_sale()'}))

    export_handling_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    freight_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))

    doc_clearance_sale = forms.DecimalField(label='Doc Clearance',
        widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    ground_handling_sale = forms.DecimalField(label='Ground Handling',
        widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    warehouse_charge_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    handling_charge_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    delivery_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))
    duty_tax_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'})) 
    tax_handling_charge_sale = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input-small ttip_t'}))

    class Meta:
        model = Sale
        fields = ('__all__')