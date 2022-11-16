from django import forms

from apps.products.models import Commodity

class CommodityForm(forms.ModelForm):
    
    class Meta:
        model = Commodity
        fields ='__all__'