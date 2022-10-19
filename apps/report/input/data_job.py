from django.shortcuts import redirect, render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from apps.products.models import Transaksi,Job
from apps.report.input.forms import UpdateForm

@login_required
def detail_job(request,pk):
    data = Job.objects.get(id=pk)
    return render(request,'pengajuan/input/dtl_job.html',{'data':data})

@login_required
def detail_job_all(request,pk):
    data = Transaksi.objects.get(id=pk)
    return render(request,'pengajuan/input/data_job_all.html',{'data':data})

@login_required
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
    return render(request,'pengajuan/input/update_job.html',{'data':data,'forms':form})


def datajob(request):
    query = request.GET.get('search')
    if query == None:
        query = ''
    object_list = Job.objects.filter(Q(transaksi__no_pekerjaan__icontains=query) | Q(vendor__nama_jasa_pengiriman__icontains=query)).order_by('id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 15) # 6 employees per page
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        
        page_obj = paginator.page(paginator.num_pages)
    return render(request,'pengajuan/input/data_job.html',{'data':page_obj})