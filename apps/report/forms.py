from dataclasses import field
from django import forms

from apps.products.models import MataUang,STATUS,Kurs

class MataUangForm(forms.ModelForm):
    negara = forms.CharField(label="Negara", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    kode_matauang = forms.CharField(label="Kode Mata Uang", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    nama_mata_uang = forms.CharField(label="Nama Mata Uang", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)
    
    class Meta:
        model = MataUang
        fields = ['id','negara','kode_matauang','nama_mata_uang','status']

class KursForm(forms.ModelForm):
    mtu = forms.ModelChoiceField(label="Nama Negara",queryset=MataUang.objects.filter(status='1'),
        widget=forms.Select(attrs={'class':'form-control transaction chosen-select'}))
    nilai_kurs = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control transaction',
        'alt':'integer'}),required =False)
    tanggal_aktif = forms.DateField(label="Tanggal Aktif", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))
    status_kurs = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select '}), choices=STATUS)
    
    class Meta:
        model = Kurs
        fields = ['id','mtu','nilai_kurs','tanggal_aktif','status_kurs']