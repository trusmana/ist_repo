from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages

from apps.products.models import ParameterData
from apps.report.parameter.paramdata import edit_forms as fparam

@login_required(login_url=settings.LOGIN_URL)
def fsedit(request,id):
    user= request.user
    data = ParameterData.objects.get(id= id)
    if request.method == "POST":
        form = fparam.FSForm(request.POST,instance=data) 
        if form.is_valid():
            form.save()  # type: ignore
            messages.success(request, 'Parameter Vendor Berhasil DiSimpan')
            return redirect('/report/list_param/%s/'%data.id ) # type: ignore
    else:
        form = fparam.FSForm(instance=data)
    return render(request,'report/parameter/edit/edit_fs.html',{'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def sledit(request,id):
    user= request.user
    data = ParameterData.objects.get(id= id)
    if request.method == "POST":
        form = fparam.SLForm(request.POST,instance=data) 
        if form.is_valid():
            form.save()  # type: ignore
            messages.success(request, 'Parameter Vendor Berhasil DiSimpan')
            return redirect('/report/list_param/%s/'%data.id ) # type: ignore
    else:
        form = fparam.SLForm(instance=data)
    return render(request,'report/parameter/edit/edit_fs.html',{'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def dledit(request,id):
    user= request.user
    data = ParameterData.objects.get(id= id)
    if request.method == "POST":
        form = fparam.DLForm(request.POST,instance=data) 
        if form.is_valid():
            form.save()  # type: ignore
            messages.success(request, 'Parameter Vendor Berhasil DiSimpan')
            return redirect('/report/list_param/%s/'%data.id ) # type: ignore
    else:
        form = fparam.DLForm(instance=data)
    return render(request,'report/parameter/edit/edit_fs.html',{'forms':form})