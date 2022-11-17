from dataclasses import field
from django import forms

from apps.products.models import Kurs, Negara, Produk,STATUS,JasaPengiriman,JENISPRODUK

class ProdukForm(forms.ModelForm):    
    nama_produk = forms.CharField(label="Nama Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction','readonly':True}))
    tgl_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'DD-mm-YYYY','readonly':True}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    jenis_produk = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=JENISPRODUK)
    origin_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    point_satu = forms.ModelChoiceField(queryset=Negara.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    kurs_origin = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)

    through_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    kurs_through = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    point_dua = forms.ModelChoiceField(queryset=Negara.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)

    destinations_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_destinations = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_tiga = forms.ModelChoiceField(queryset=Negara.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))

    class Meta:
        model = Produk
        fields =['jumlah_vendor','id','nama_produk','tgl_aktif','status','jenis_produk','origin_vendor','point_satu',
            'kurs_origin','through_vendor','point_dua','kurs_through','destinations_vendor','kurs_destinations',
            'point_tiga']

class ProdukDuaForm(forms.ModelForm):
    nama_produk = forms.CharField(label="Nama Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction','readonly':True}))
    tgl_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'DD-mm-YYYY','readonly':True}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    jenis_produk = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction chosen-select',}), choices=JENISPRODUK)
    origin_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction chosen-select'}),required=False)
    point_satu = forms.ModelChoiceField(queryset=Negara.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}),required=False)
    kurs_origin = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}),required=False)
    
    destinations_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    kurs_destinations = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))
    point_tiga = forms.ModelChoiceField(queryset=Negara.objects.filter(status=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control chosen-select'}))

    class Meta:
        model = Produk
        fields =['jumlah_vendor','nama_produk','tgl_aktif','status','origin_vendor','point_satu',
            'kurs_origin','destinations_vendor','kurs_destinations','point_tiga']