from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.views import View
from django.template import loader
from django.contrib import messages
from django.http import JsonResponse,HttpResponse,QueryDict
from django.template.loader import render_to_string
from django.urls import reverse
from apps.utils import set_pagination


from apps.products import models as mp
from apps.paramvendor.invoice import forms as fv


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class list_shiper(View):
    context = {'segment': 'transactions'}

    def get(self, request, pk=None, action=None):
        if is_ajax(request=request):
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)  # type: ignore
    
    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('list_shipper')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Data Berhasil Di Hapus')
            redirect_url = reverse('list_shipper')

        response = {'valid': 'success', 'message': 'Data Berhasil Di Hapus', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(nama__icontains=key.strip())
                    else:
                        filter_params |= Q(nama__icontains=key.strip())

        transactions = mp.ShipperInvoice.objects.filter(filter_params) if filter_params else mp.ShipperInvoice.objects.all().order_by('id')

        self.context['transactions'], self.context['info'] = set_pagination(request, transactions)# type: ignore
        if not self.context['transactions']:
            return False, self.context['info']

        return self.context, 'menu_invoice/shipper/invoice_shipper.html'

    def edit(self, request, pk):
        transaction = self.get_object(pk)

        self.context['transaction'] = transaction # type: ignore
        self.context['form'] = fv.ShipperForm(instance=transaction)# type: ignore

        return self.context, 'menu_invoice/shipper/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        transaction = self.get_object(pk)
        form = fv.ShipperForm(instance=transaction)
        context = {'instance': transaction, 'form': form}
        return render_to_string('menu_invoice/shipper/edit_row.html', context)

    """ Common methods """
        
    def get_object(self, pk):
        transaction = get_object_or_404(mp.ShipperInvoice, id=pk)
        return transaction
    
    def get_row_item(self, pk):
        transaction = self.get_object(pk)
        edit_row = render_to_string('menu_invoice/shipper/edit_row.html', {'instance': transaction})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = fv.ShipperForm(form_data, instance=transaction)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Data Berhasil DiSimpan')

            return True, 'Data Berhasil DiSimpan'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    

@login_required(login_url=settings.LOGIN_URL)
def addshipper(request):
    user = request.user
    if request.method == 'POST':
        form = fv.ShipperForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.cu = user
            prod.save()
            messages.success(request, 'Data Berhasil Di simpan')
            return redirect('list_shipper')
    else:
        form = fv.ShipperForm(initial={'status':1})
    return render(request,'menu_invoice/shipper/add_alt_shipper.html',{'form':form})