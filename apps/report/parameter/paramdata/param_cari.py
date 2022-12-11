from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings

from apps.report.parameter.paramdata.form import CariForm,CariDuaForm
from apps.products.models import Produk

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT','OPERASIONAL')))  # type: ignore
def addparamdta(request):
    if request.method == 'POST':
        form = CariForm(request.POST)
        if form.is_valid():
            pr = form.cleaned_data['products']
            aa = Produk.objects.get(id=pr.id)
            if aa.jumlah_vendor == '3':
                messages.success(request, 'Data Parameter %s %s %s'%(aa.origin_vendor.id,aa.through_vendor.id,aa.destinations_vendor.id) )  # type: ignore
                return redirect('/report/add_paramdata/%s/%s/%s/%s/'%(aa.id,aa.origin_vendor.id,aa.through_vendor.id,aa.destinations_vendor.id))  # type: ignore
            else:
                print('test 3')
                messages.success(request, 'Data Parameter Belum Ada')
                #return redirect('in-pengajuan')
    else:
        form = CariForm()
    return render(request,'report/parameter/addparamcari.html',{'form':form})

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT','OPERASIONAL')))  # type: ignore
def addparamdtadua(request):
    if request.method == 'POST':
        form = CariDuaForm(request.POST)
        if form.is_valid():
            pr = form.cleaned_data['products']
            aa = Produk.objects.get(id=pr.id)
            if aa.jumlah_vendor == '2':
                print(aa.origin_vendor.id,'origin','destina', aa.destinations_vendor.id)  # type: ignore
                messages.success(request, 'Data Parameter DL FS %s %s'%(aa.origin_vendor.id,aa.destinations_vendor.id) )  # type: ignore
                return redirect('/report/add_paramdatadua/%s/%s/%s/'%(aa.id,aa.origin_vendor.id,aa.destinations_vendor.id))  # type: ignore
                
            else:
                print('test 3')
                messages.success(request, 'Data Parameter Belum Ada')
                #return redirect('in-pengajuan')
    else:
        form = CariDuaForm()
    return render(request,'report/parameter/addparamcari.html',{'form':form})