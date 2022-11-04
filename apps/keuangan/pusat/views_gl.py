from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
import datetime

from apps.keuangan.models import Jurnal_History,Tbl_Transaksi,Tbl_Transaksi_History,Jurnal,Tbl_Akun
from apps.keuangan.pusat.forms_gl import get_ordereditem_formset,MainJurnalglForm,MainJurnalForm

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.groups.filter(name__in=('KEUANGAN','Administrator')))
def gl_gl_pusat(request,form_class):
    user = request.user
    kocab= user.profile.cabang.id
    sekarang = datetime.date.today()
    Tbl_Transaksi_History_glFormset = get_ordereditem_formset(form_class, extra=1, can_delete=True)    
    show = Tbl_Transaksi.objects.filter(status_jurnal=1,jurnal__cu__id = user.id,id_cabang=kocab).filter(tgl_trans= sekarang)
    order = Tbl_Transaksi_History.objects.all()
    if request.method == 'POST':
        form = MainJurnalglForm(request.POST)
        formset = Tbl_Transaksi_History_glFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            tgl_trans = form.cleaned_data['tgl_trans']
            jurnal = Jurnal_History.objects.create(tgl_trans=tgl_trans,diskripsi='GL_GL_PUSAT',kode_cabang=user.profile.cabang.kode_cabang)
            jurnal_asli = Jurnal.objects.create(tgl_trans=tgl_trans,diskripsi='GL_GL_PUSAT_BANK',
                cu=user,mu=user,kode_cabang=user.profile.cabang.kode_cabang)
            for itemform in formset.forms:
                koderekening = itemform.cleaned_data['koderekening']
                kdd = koderekening[:12]
                if koderekening:
                    rekening = Tbl_Akun.objects.get(coa=kdd)                    
                    if not rekening:
                        messages.add_message(request, messages.INFO,"Kode Rekening Tidak Ditemukan")
                        return redirect('/gl_gl_pusat/')
                    debet = itemform.cleaned_data['debet']
                    kredit = itemform.cleaned_data['kredit']
                    deskripsi = itemform.cleaned_data['deskripsi']
                    debet = debet
                    kredit = kredit
                    if jurnal.j_status == '1':
                        itemjurnal = Tbl_Transaksi_History.objects.create(id_coa= rekening,debet=debet,kredit=kredit,\
                            tgl_trans=tgl_trans,no_trans =jurnal.no_akad,jurnal_h = jurnal,id_product=4,status_jurnal=1,\
                            id_cabang=kocab,id_unit=100,jenis='GL_GL_PUSAT_BANK',deskripsi=deskripsi)
                        itemju = Tbl_Transaksi.objects.create(id_coa= rekening,debet=debet,kredit=kredit,tgl_trans=tgl_trans,\
                            no_trans =jurnal.no_akad,jurnal = jurnal_asli,id_product=4,status_jurnal=1,id_cabang=0,id_unit=100,\
                            jenis='GL_GL_PUSAT_BANK',deskripsi=deskripsi)
                    else:
                        itemjurnal = Tbl_Transaksi_History.objects.create(id_coa= rekening,debet=debet,kredit=kredit,tgl_trans=tgl_trans,\
                            no_trans =jurnal.no_akad,jurnal_h = jurnal,id_product=4,status_jurnal=1,id_cabang=kocab,id_unit=100,\
                            jenis='GL_GL_PUSAT',deskripsi=deskripsi)
                        itemju = Tbl_Transaksi.objects.create(id_coa= rekening,debet=debet,kredit=kredit,tgl_trans=tgl_trans,\
                            no_trans =jurnal.no_akad,jurnal = jurnal_asli,id_product=4,status_jurnal=1,id_cabang=kocab,id_unit=100,\
                            jenis='GL_GL_PUSAT',deskripsi=deskripsi)              
                messages.add_message(request, messages.INFO,"Jurnal telah disimpan dengan sukses")
            return redirect('.')
        else:
            messages.add_message(request, messages.INFO,"Form Tidak Valid")
            var = {'formset': formset,'show':jurnal}
            return redirect('/gl_gl_pusat/',var)
    else:
        return render(request, 'keuangan/add_gl_pusat.html', {'form': MainJurnalForm(),\
            'formset': Tbl_Transaksi_History_glFormset(),'show':show})