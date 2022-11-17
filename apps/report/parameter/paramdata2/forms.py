from dataclasses import field, fields
from django import forms

from apps.products.models import ParameterDataBl,Kurs

class ParamDuaForm(forms.ModelForm):
    tgl_aktif_param = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction ','readonly':True}))
    nilai_kurs = forms.ModelChoiceField(queryset=Kurs.objects.filter(status_kurs=1).order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    '''
    id_prod = forms.CharField(label="ID Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    nama_produk = forms.CharField(label="Nama Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    tgl_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    origin_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_satu = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_origin = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))

    through_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_through = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_dua = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
from django import forms
from apps.products.models import ParameterDataBl

class ParamDuaForm(forms.ModelForm):
    tgl_aktif_param = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction ','readonly':True}))
    '''
    id_prod = forms.CharField(label="ID Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    nama_produk = forms.CharField(label="Nama Produk", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    tgl_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    origin_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_satu = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_origin = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))

    through_vendor = forms.ModelChoiceField(queryset=JasaPengiriman.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    kurs_through = forms.ModelChoiceField(queryset=Kurs.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
    point_dua = forms.ModelChoiceField(queryset=Negara.objects.all().order_by('id'),
        widget=forms.Select(attrs={'class':'form-control transaction'}))
