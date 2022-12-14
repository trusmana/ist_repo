from django.shortcuts import redirect, render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from apps.products.models import Transaksi,Job,Sale
from apps.report.input.forms import UpdateForm
from apps.report.job.forms import RefForm,KursDutyForm,HeaderInvForm
from django import forms
from django.forms.widgets import HiddenInput

@login_required(login_url=settings.LOGIN_URL)
def header_invoice(request, pk):
    user = request.user
    sale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        form = HeaderInvForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ref Customer Berhasil Di Input')
            return redirect('/report/dtl_all_job/%s/' %(sale.trans.id))  # type: ignore
    else:
        form = HeaderInvForm()  # type: ignore
    return render(request,'job/header_invoice.html',{'sale':sale,'form':form})


@login_required(login_url=settings.LOGIN_URL)
def edit_kursduty(request, pk):
    user = request.user
    sale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        form = KursDutyForm(request.POST,instance= sale)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ref Customer Berhasil Di Input')
            return redirect('/report/dtl_all_job/%s/' %(sale.trans.id)  )  # type: ignore
    else:
        form = KursDutyForm(instance=sale)  # type: ignore
    return render(request,'job/edit_kursduty.html',{'sale':sale,'form':form})

@login_required(login_url=settings.LOGIN_URL)
def add_ref(request, pk):
    user = request.user
    sale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        form = RefForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ref Customer Berhasil Di Input')
            return redirect('/report/dtl_all_job/%s/' %(sale.trans.id)  )  # type: ignore
    else:
        form = RefForm(initial={'fkref':sale.id})  # type: ignore
        form.fields["fkref"].widget = forms.HiddenInput()
    return render(request,'job/add_ref.html',{'sale':sale,'form':form})


@login_required(login_url=settings.LOGIN_URL)
def detail_job(request,pk):
    data = Job.objects.get(id=pk)
    return render(request,'job/dtl_job.html',{'data':data})

@login_required(login_url=settings.LOGIN_URL)
def detail_job_all(request,pk):
    data = Transaksi.objects.get(id=pk)
    return render(request,'job/data_job_all.html',{'data':data})

@login_required(login_url=settings.LOGIN_URL)
def update_job(request,pk):
    user = request.user
    data = Job.objects.get(id=pk)
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            status = form.cleaned_data['status']
            data.tanggal_status = tanggal
            data.status_job = status
            data.cu_update = user
            data.save()
            messages.success(request, 'Status Pekerjaan Berhasil Di Update')
            return redirect('d-job')
            
    else:
        form = UpdateForm(initial={'tanggal':datetime.date.today()})
    return render(request,'job/update_job.html',{'data':data,'forms':form})

@login_required(login_url=settings.LOGIN_URL)
#####Data pekerjaan On Proses
def datajob(request):
    query = request.GET.get('search')
    if query == None:
        query = ''
    object_list = Job.objects.filter(Q(transaksi__no_pekerjaan__icontains=query) | Q(vendor__nama_jasa_pengiriman__icontains=query),status_job__isnull =True).order_by('id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 12) 
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'job/data_job.html',{'data':page_obj})

@login_required(login_url=settings.LOGIN_URL)
#####Data pekerjaan On Proses
def datajob_done(request):
    query = request.GET.get('search')
    if query == None:
        query = ''
    object_list = Job.objects.filter(Q(transaksi__no_pekerjaan__icontains=query) | Q(vendor__nama_jasa_pengiriman__icontains=query),status_job__isnull =False).order_by('id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 12) 
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'job/data_job_done.html',{'data':page_obj})