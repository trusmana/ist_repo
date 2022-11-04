from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
import datetime,decimal

from apps.keuangan.models import BiayaPusat, Tbl_Transaksi,BiayaMapper,Jurnal
from apps.keuangan.forms import BiayaForm

@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=('KEUANGAN','Administrator')))
def hapus_jurnal(request,id):
    tbl = Jurnal.objects.get(id=id)
    tbl.delete()
    messages.add_message(request, messages.INFO, 'Penghapusan Jurnal Berhasil')
    return redirect("i-biaya")

@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=('KEUANGAN','Administrator')))
def input_gl(request):
    user = request.user
    sekarang = datetime.date.today()
    bea = Tbl_Transaksi.objects.filter(tgl_trans=sekarang).filter(status_jurnal = 1).\
        filter(jenis__in=( u'BIAYA_UANG_MUKA',u'BIAYA_KAS'))
    if request.method == "POST":
        form = BiayaForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            listrik = form.cleaned_data['listrik']
            ket_listrik = form.cleaned_data['ket_listrik']
            pdam  = form.cleaned_data['pdam']
            ket_pdam = form.cleaned_data['ket_pdam']
            telpon = form.cleaned_data['telpon']
            ket_telpon = form.cleaned_data['ket_telpon']
            
            palkir = form.cleaned_data['palkir']
            ket_palkir = form.cleaned_data['ket_palkir']
            bbm = form.cleaned_data['bbm']
            ket_bbm = form.cleaned_data['ket_bbm']
            
            pemb_lingkungan = form.cleaned_data['pemb_lingkungan']
            ket_pemb_lingkungan = form.cleaned_data['ket_pemb_lingkungan']
            sumbangan = form.cleaned_data['sumbangan']
            ket_sumbangan = form.cleaned_data['ket_sumbangan']
            perlengkapan = form.cleaned_data['perlengkapan']
            ket_perlengkapan = form.cleaned_data['ket_perlengkapan']
            konsumsi = form.cleaned_data['konsumsi']
            ket_konsumsi = form.cleaned_data['ket_konsumsi']
            foto_copy  = form.cleaned_data['foto_copy']
            ket_foto_copy = form.cleaned_data['ket_foto_copy']
            lain_lain = form.cleaned_data['lain_lain']
            ket_lain_lain = form.cleaned_data['ket_lain_lain']

            jenis_transaksi_listrik = form.cleaned_data['jenis_transaksi_listrik']
            jenis_transaksi_pdam= form.cleaned_data['jenis_transaksi_pdam']
            jenis_transaksi_telepon= form.cleaned_data['jenis_transaksi_telepon']
            jenis_transaksi_foto_copy= form.cleaned_data['jenis_transaksi_foto_copy']
            
            jenis_transaksi_palkir      = form.cleaned_data['jenis_transaksi_palkir']
            jenis_transaksi_bbm = form.cleaned_data['jenis_transaksi_bbm']
            
            jenis_transaksi_pemb_lingkungan     = form.cleaned_data['jenis_transaksi_pemb_lingkungan']
            jenis_transaksi_sumbangan   = form.cleaned_data['jenis_transaksi_sumbangan']
            jenis_transaksi_perlengkapan = form.cleaned_data['jenis_transaksi_perlengkapan']
            jenis_transaksi_konsumsi    = form.cleaned_data['jenis_transaksi_konsumsi']
            
            jenis_transaksi_biaya_bank = form.cleaned_data['jenis_transaksi_biaya_bank']
            biaya_bank = form.cleaned_data['biaya_bank']
            ket_biaya_bank = form.cleaned_data['ket_biaya_bank']
            jenis_transaksi_pengiriman = form.cleaned_data['jenis_transaksi_pengiriman']
            pengiriman = form.cleaned_data['pengiriman']
            ket_pengiriman = form.cleaned_data['ket_pengiriman']
            jenis_transaksi_entertaint = form.cleaned_data['jenis_transaksi_entertaint']
            entertaint = form.cleaned_data['entertaint']
            ket_entertaint = form.cleaned_data['ket_entertaint']

            biaya = BiayaPusat(cabang = user.profile.cabang,tanggal = tanggal,listrik = listrik,ket_listrik = ket_listrik,\
                pdam  = pdam,ket_pdam = ket_pdam,telpon = telpon,ket_telpon = ket_telpon,
                palkir = palkir,ket_palkir = ket_palkir,bbm = bbm,ket_bbm = ket_bbm,
                foto_copy = foto_copy,ket_foto_copy = ket_foto_copy,
                pemb_lingkungan= pemb_lingkungan,ket_pemb_lingkungan= ket_pemb_lingkungan,\
                sumbangan = sumbangan,ket_sumbangan = ket_sumbangan,perlengkapan = perlengkapan,\
                ket_perlengkapan = ket_perlengkapan, konsumsi = konsumsi,ket_konsumsi = ket_konsumsi,\
                jenis_transaksi_listrik= jenis_transaksi_listrik,jenis_transaksi_pdam= jenis_transaksi_pdam,\
                jenis_transaksi_telepon = jenis_transaksi_telepon,jenis_transaksi_foto_copy= jenis_transaksi_foto_copy,
                jenis_transaksi_palkir= jenis_transaksi_palkir,\
                jenis_transaksi_bbm     = jenis_transaksi_bbm,
                jenis_transaksi_pemb_lingkungan= jenis_transaksi_pemb_lingkungan,\
                jenis_transaksi_sumbangan= jenis_transaksi_sumbangan,jenis_transaksi_konsumsi= jenis_transaksi_konsumsi,\
                jenis_transaksi_perlengkapan= jenis_transaksi_perlengkapan,jenis_transaksi_biaya_bank = jenis_transaksi_biaya_bank,\
                biaya_bank = biaya_bank,ket_biaya_bank = ket_biaya_bank,jenis_transaksi_pengiriman = jenis_transaksi_pengiriman,\
                pengiriman = pengiriman,ket_pengiriman = ket_pengiriman,
                jenis_transaksi_entertaint = jenis_transaksi_entertaint, entertaint = entertaint,\
                ket_entertaint = ket_entertaint)
                
            biaya.save()
            if biaya.listrik > 0:
                jurnal_biaya_listrik(biaya, request.user)
            elif biaya.pdam > 0:
                jurnal_biaya_pdam(biaya, request.user)
            elif biaya.telpon > 0:
                jurnal_biaya_telepon(biaya, request.user)
            
            elif biaya.palkir > 0:
                jurnal_biaya_palkir(biaya, request.user)
            elif biaya.bbm > 0:
                jurnal_biaya_bbm(biaya, request.user)
            elif biaya.pemb_lingkungan > 0:
                jurnal_biaya_pemb_lingkungan(biaya, request.user)   
            elif biaya.konsumsi > 0:
                jurnal_biaya_konsumsi(biaya, request.user) 
            elif biaya.sumbangan > 0:
                jurnal_biaya_sumbangan(biaya, request.user)
            elif biaya.perlengkapan > 0:
                jurnal_biaya_perlengkapan(biaya, request.user)
            elif biaya.foto_copy > 0:
                jurnal_biaya_foto_copy(biaya, request.user)
            elif biaya.lain_lain > 0:
                jurnal_biaya_lain_lain(biaya, request.user) 
            elif biaya.entertaint > 0:
                jurnal_biaya_entertaint(biaya, request.user)
            messages.add_message(request, messages.INFO,"JURNAL Berhasil ")
            return redirect('i-biaya')
    else:
        form  = BiayaForm()
        return render(request,'keuangan/biaya/biaya.html',{'user':user,'form':form,'bea':bea})

def jurnal_biaya_entertaint(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_entertaint,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_entertaint == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_entertaint,
            kredit = 0,debet = D((biaya.entertaint)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_entertaint,
            debet = 0,kredit = D((biaya.entertaint)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)
    else:
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi =biaya.ket_entertaint,
            kredit = 0,debet = D((biaya.entertaint)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi=biaya.ket_entertaint,
            debet = 0,kredit = D((biaya.entertaint)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_lain_lain(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_lain_lain,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_lain_lain == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_lain_lain,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_lain_lain,
            debet = 0,kredit = D((biaya.lain_lain)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_lain_lain == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi =biaya.ket_lain_lain,
            kredit = 0,debet = D((biaya.lain_lain)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_lain_lain,
            debet = 0,kredit = D((biaya.lain_lain)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)


def jurnal_biaya_foto_copy(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_foto_copy,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_foto_copy == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_foto_copy,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_foto_copy,
            debet = 0,kredit = D((biaya.foto_copy)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_foto_copy == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi =biaya.ket_foto_copy,
            kredit = 0,debet = D((biaya.foto_copy)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi=biaya.ket_foto_copy,
            debet = 0,kredit = D((biaya.foto_copy)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_perlengkapan(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_perlengkapan,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_perlengkapan == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_perlengkapan,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_perlengkapan,
            debet = 0,kredit = D((biaya.perlengkapan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_perlengkapan == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_perlengkapan,
            kredit = 0,debet = D((biaya.perlengkapan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi=biaya.ket_perlengkapan,
            debet = 0,kredit = D((biaya.perlengkapan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_sumbangan(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_sumbangan,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_sumbangan == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_sumbangan,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_sumbangan,
            debet = 0,kredit = D((biaya.sumbangan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_sumbangan == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_sumbangan,
            kredit = 0,debet = D((biaya.sumbangan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_sumbangan,
            debet = 0,kredit = D((biaya.sumbangan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_konsumsi(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_konsumsi,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_konsumsi == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_konsumsi,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_konsumsi,
            debet = 0,kredit = D((biaya.konsumsi)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_konsumsi == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_konsumsi,
            kredit = 0,debet = D((biaya.konsumsi)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_konsumsi,
            debet = 0,kredit = D((biaya.konsumsi)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_pemb_lingkungan(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_pemb_lingkungan,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_pemb_lingkungan == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_pemb_lingkungan,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_pemb_lingkungan,
            debet = 0,kredit = D((biaya.pemb_lingkungan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_pemb_lingkungan == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_pemb_lingkungan,
            kredit = 0,debet = D((biaya.pemb_lingkungan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
    
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_pemb_lingkungan,
            debet = 0,kredit = D((biaya.pemb_lingkungan)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)


def jurnal_biaya_bbm(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_bbm,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_bbm == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_bbm,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_bbm,
            debet = 0,kredit = D((biaya.bbm)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_bbm == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_bbm,
            kredit = 0,debet = D((biaya.bbm)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_bbm,
            debet = 0,kredit = D((biaya.bbm)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)


def jurnal_biaya_palkir(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_palkir,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_palkir == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_palkir,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_palkir,
            debet = 0,kredit = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_palkir == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_palkir,
            kredit = 0,debet = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_palkir,
            debet = 0,kredit = D((biaya.palkir)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)


##### LISTRIK
def jurnal_biaya_listrik(biaya, user):
    D = decimal.Decimal
    
    jurnal = Jurnal.objects.create(diskripsi=biaya.ket_listrik,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_listrik == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_listrik,
            kredit = 0,debet = D((biaya.listrik)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"), deskripsi =biaya.ket_listrik,
            debet = 0,kredit = D((biaya.listrik)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_listrik == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"), deskripsi =biaya.ket_listrik,
            kredit = 0,debet = D((biaya.listrik)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_listrik,
            debet = 0,kredit = D((biaya.listrik)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_pdam(biaya, user):
    D = decimal.Decimal
    
    jurnal = Jurnal.objects.create(diskripsi= biaya.ket_pdam,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_pdam == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_pdam,
            kredit = 0,debet = D((biaya.pdam)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_pdam,
            debet = 0,kredit = D((biaya.pdam)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)
    elif biaya.jenis_transaksi_pdam == '1':###KAS
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_pdam,
            kredit = 0,debet = D((biaya.pdam)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_pdam,
            debet = 0,kredit = D((biaya.pdam)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

def jurnal_biaya_telepon(biaya, user):
    D = decimal.Decimal
    jurnal = Jurnal.objects.create(diskripsi= biaya.ket_telpon,kode_cabang = biaya.cabang.kode_cabang,object_id=biaya.id,\
        tgl_trans = biaya.tanggal,cu = user, mu = user)
    if biaya.jenis_transaksi_telepon == '2':###Uang Muka
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_telpon,
            kredit = 0,debet = D((biaya.telpon)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_UANG_MUKA"),deskripsi =biaya.ket_telpon,
            debet = 0,kredit = D((biaya.telpon)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)

    elif biaya.jenis_transaksi_telepon == '1':###Kas
        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi =biaya.ket_telpon,
            kredit = 0,debet = D((biaya.telpon)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang =biaya.cabang.kode_cabang)

        jurnal.tbl_transaksi_set.create(jenis = '%s' % ("BIAYA_KAS"),deskripsi=biaya.ket_telpon,
            debet = 0,kredit = D((biaya.telpon)),id_product = '4',status_jurnal ='1',tgl_trans =biaya.tanggal,
            id_cabang = biaya.cabang.kode_cabang)
