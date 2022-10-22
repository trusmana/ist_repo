import django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from traitlets import Instance

from apps.products.models import Sale
from apps.report.input.edit_inputan.form import JualForm

@login_required(login_url=settings.LOGIN_URL)
def edit_jual(request,id):
    jual = Sale.objects.get(pk=id)
    if request.method == 'POST':
        form = JualForm(request.POST,instance=jual)
        if form.is_valid():
            form.save()
            return redirect('/detail/%s/' %(jual.id))
    else:
        form = JualForm(instance=jual)
    return render(request,'pengajuan/input/edit/edit_jual.html',{'data':jual,'forms':form})