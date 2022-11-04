from django import forms
from django.forms.formsets import formset_factory
from django.forms import models
import datetime
from apps.keuangan.models import Jurnal_History,Tbl_Transaksi_History,J_STATUS

def get_ordereditem_formset(form, formset=models.BaseInlineFormSet, **kwargs):
    return models.inlineformset_factory(Jurnal_History, Tbl_Transaksi_History, form, formset, **kwargs)

class MainJurnalglForm(forms.Form):
    tgl_trans = forms.DateField(initial=datetime.date.today,widget=forms.widgets.DateInput(attrs={'readonly':'true'}, format="%d-%m-%Y"))

class MainJurnalForm(forms.Form):
    tgl_trans = forms.DateField(label="Tanggal",initial=datetime.date.today(),widget=forms.widgets.DateInput(attrs={'readonly':'true'}, format="%d-%m-%Y"))
    j_status = forms.ChoiceField(label ="Status",widget=forms.RadioSelect,choices=J_STATUS,initial = '0',required = False)
