from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
import datetime

from apps.report.parameter.sale.forms import SaleForm
from apps.products.models import Sale
from apps.report.input.forms import UpdateForm
@login_required(login_url=settings.LOGIN_URL)
#####Data Sale On Proses
def datasaledone(request):
    query = request.GET.get('search')
    if query == None:
        query = ''
    object_list = Sale.objects.filter(status_sale__isnull=False).order_by('id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 12) 
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'report/sale/data_sale_done.html',{'data':page_obj})



@login_required(login_url=settings.LOGIN_URL)
#####Data Sale On Proses
def datasale(request):
    query = request.GET.get('search')
    if query == None:
        query = ''
    object_list = Sale.objects.filter(status_sale__isnull=True).order_by('id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 12) 
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'report/sale/data_sale.html',{'data':page_obj})

@login_required(login_url=settings.LOGIN_URL)
def update_sale(request,pk):
    data = Sale.objects.get(id=pk)
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            status = form.cleaned_data['status']
            data.tgl_done = tanggal
            data.status_sale = status
            data.save()
            messages.success(request, 'Status Sale Berhasil Di Update')
            return redirect('d-sale')            
    else:
        form = UpdateForm(initial={'tanggal':datetime.date.today()}) # type: ignore
    return render(request,'report/sale/update_sale.html',{'data':data,'forms':form})

    
@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT','OPERASIONAL')))  # type: ignore
def editsale(request,id):
    data = Sale.objects.get(pk=id)
    user = request.user
    if request.method == 'POST':
        form = SaleForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,'Data Param Berhasil Di Input', 'alert-success')
            return redirect('d-sale')
    else:
        form = SaleForm(instance=data)
    return render(request,'report/sale/edit_sale.html',{'form':form,'sale':data})

