from django import forms

from apps.products.models import JasaPengiriman,STATUS

class PengirimanForm(forms.ModelForm):
    nama_jasa_pengiriman = forms.CharField(label="Nama Vendor", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    alamat =  forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    telepon =  forms.CharField(label="Telepon", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)

    class Meta:
        model = JasaPengiriman
        fields =['id','nama_jasa_pengiriman','alamat','telepon','status','singkatan']