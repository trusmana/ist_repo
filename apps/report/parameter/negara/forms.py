from django import forms

from apps.products.models import Negara,STATUS

class NegaraForm(forms.ModelForm):
    nama_negara = forms.CharField(label="Nama Negara", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    nama_kota = forms.CharField(label="Nama Kota", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    singkatan = forms.CharField(label="Singkatan", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control transaction'}), choices=STATUS)

    class Meta:
        model = Negara
        fields =['id','nama_negara','nama_kota','singkatan','status']