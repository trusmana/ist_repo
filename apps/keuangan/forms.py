from django import forms
from django.forms import models
import datetime

from apps.keuangan.models import JS_TRANSAKSI,JS_TRANSAKSI_BANK,AKUN_PILIH,Tbl_Transaksi_History,J_STATUS

class Tbl_Transaksi_History_glForm(models.ModelForm):
    deskripsi = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'size': 30,'class':'form-control'}))
    koderekening = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'kode_rekening form-control','size':40}),
        required = False)
    debet = forms.FloatField(widget=forms.TextInput(attrs={'size': 9, 'class': 'rp_debet uang form-control',
        'value': '0', 'alt': 'integer'}),required = False)
    kredit = forms.FloatField(widget=forms.TextInput(attrs={'size': 9, 'class': 'rp_kredit uang form-control',
        'value': '0', 'alt': 'integer'}),required = False)
    j_status = forms.ChoiceField(label ="Status",widget=forms.RadioSelect,choices= J_STATUS,
         initial = '3',required = False)
    class Meta:
        model = Tbl_Transaksi_History
        fields=('id_coa', 'kredit', 'debet','deskripsi')

class BiayaForm(forms.Form):
    tanggal = forms.DateField(initial = datetime.date.today,widget=forms.widgets.DateInput(attrs={'readonly':'true'}, format="%d-%m-%Y"))
    listrik = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_listrik = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    pdam  = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_pdam = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    telpon = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_telpon = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    
    palkir = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':25}))
    ket_palkir = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    bbm = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}))
    ket_bbm = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    
    pemb_lingkungan = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}))
    ket_pemb_lingkungan = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    foto_copy  = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_foto_copy = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    sumbangan  = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_sumbangan = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    konsumsi  = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_konsumsi = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    perlengkapan  = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10,}))
    ket_perlengkapan = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    lain_lain = forms.ChoiceField(widget=forms.Select(), choices=AKUN_PILIH,required = False)
    ket_lain_lain = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    penerimaan_saldo = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}),required = False)
    saldo_awal = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}),required = False)
    saldo_akhir = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}),required = False)
    jenis_transaksi_listrik     = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_pdam        = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_telepon     = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_foto_copy   = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_majalah     = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_palkir      = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_bbm = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)

    jenis_transaksi_nilai_lain_lain= forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_pemb_lingkungan= forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_sumbangan= forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_perlengkapan= forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_konsumsi= forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    jenis_transaksi_biaya_bank = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI_BANK,required = False)
    biaya_bank = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}))
    ket_biaya_bank = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
    jenis_transaksi_pengiriman = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    pengiriman = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}))
    ket_pengiriman = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)

    jenis_transaksi_entertaint = forms.ChoiceField(widget=forms.Select(), choices=JS_TRANSAKSI,required = False)
    entertaint = forms.IntegerField(widget=forms.TextInput(attrs={'alt': 'integer', 'class': 'uang','value':0,'size':10}))
    ket_entertaint = forms.CharField( widget=forms.TextInput(attrs={'size':25,'placeholder':'Keterangan'}),required = False)
