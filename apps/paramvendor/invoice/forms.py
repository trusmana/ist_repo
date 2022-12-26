from dataclasses import field
from django import forms

from apps.products import models as mp

class InvAddressForm(forms.ModelForm):
    nama = forms.CharField(label="Head Invoice", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    alamat = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    telepon = forms.CharField(label="telepon", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    
    class Meta:
        model = mp.AddresInvoice
        fields = ['nama','alamat','telepon','status']

class ShipperForm(forms.ModelForm):
    nama = forms.CharField(label="Nama Shipper", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    alamat = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class': 'form-control transaction'}),required=False)
    kota = forms.CharField(label="Kota", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    telepon = forms.CharField(label="telepon", widget=forms.TextInput(attrs={'class': 'form-control transaction'}),required=False)
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    
    class Meta:
        model = mp.ShipperInvoice
        fields = ['nama','alamat','kota','telepon','status']

class ConsigneForm(forms.ModelForm):
    nama = forms.CharField(label="Nama Consigne", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    alamat = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class': 'form-control transaction'}),required=False)
    kota = forms.CharField(label="Kota", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    telepon = forms.CharField(label="telepon", widget=forms.TextInput(attrs={'class': 'form-control transaction'}),required=False)
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    
    class Meta:
        model = mp.ConsigneInvoice
        fields = ['nama','alamat','kota','telepon','status']

class TermForm(forms.ModelForm):
    nama_term = forms.CharField(label="Nama Term", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    class Meta:
        model = mp.TermInvoice
        fields = ['nama_term','status']

class DDpForm(forms.ModelForm):
    nama_ddp = forms.CharField(label="Nama DDP", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    class Meta:
        model = mp.DdpInvoice
        fields = ['nama_ddp','status']

class PICForm(forms.ModelForm):
    nama_pic = forms.CharField(label="Nama PIC", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=mp.STATUS)
    class Meta:
        model = mp.PicInvoice
        fields = ['nama_pic','status']

class HscForm(forms.ModelForm):
    class Meta:
        model = mp.Invoice
        fields= ['address_header','shipper','consignee','status']