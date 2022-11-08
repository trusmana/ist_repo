from dataclasses import field
from django import forms

from apps.products.models import Kurs, Negara, Produk,STATUS,JasaPengiriman,JENISPRODUK


class ProdukForm(forms.ModelForm):
    id_prod = forms.CharField(label="ID Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    nama_produk = forms.CharField(label="Nama Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    tgl_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'DD-mm-YYYY','readonly':True}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    jenis_produk = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=JENISPRODUK)
    origin_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    point_satu = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    kurs_origin = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)

    through_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    kurs_through = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)
    point_dua = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}),required=False)

    destinations_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_destinations = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_tiga = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))

    class Meta:
        model = Produk
        fields =['jumlah_vendor','id_prod','nama_produk','tgl_aktif','status','origin_vendor','point_satu',
            'kurs_origin','through_vendor','point_dua','kurs_through','destinations_vendor','kurs_destinations','point_tiga']