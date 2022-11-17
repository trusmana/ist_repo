from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.views import View
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import JsonResponse,HttpResponse,QueryDict
from django.template.loader import render_to_string
from django.urls import reverse
from apps.utils import set_pagination
from apps.products.models import ParameterData
from apps.report.parameter.paramdata.form import ParamForm,FSForm

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class list_param(View):
    context = {'segment': 'param'}

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

        return render(request, template, context)
    
    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('d-param')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        param = self.get_object(pk)
        param.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Data Berhasil Di Hapus')
            redirect_url = reverse('d-param')

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
                        filter_params = Q(products__nama_produk__icontains=key.strip())
                    else:
                        filter_params |= Q(products__nama_produk__icontains=key.strip())

        param = ParameterData.objects.filter(filter_params) if filter_params else ParameterData.objects.filter(j_vendor='3').order_by('-id')
        self.context['param'], self.context['info'] = set_pagination(request, param)
        if not self.context['param']:
            return False, self.context['info']

        return self.context, 'report/parameter/data_parameter.html'

    def edit(self, request, pk):
        param = self.get_object(pk)

        self.context['param'] = param
        self.context['form'] = FSForm(instance=param)

        return self.context, 'report/parameter/edit_parameter.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        produk = self.get_object(pk)
        form = ParamForm(instance=produk)
        context = {'instance': produk, 'form': form}
        return render_to_string('report/parameter/edit_parameter_row.html', context)

    """ Common methods """
        
    def get_object(self, pk):
        param = get_object_or_404(ParameterData, id=pk)
        return param
    
    def get_row_item(self, pk):
        pengiriman = self.get_object(pk)
        edit_row = render_to_string('report/parameter/edit_parameter_row.html', {'instance': pengiriman})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = ParamForm(form_data, instance=transaction)        
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Parameter Data Berhasil DiSimpan')

            return True, 'Parameter Data Berhasil DiSimpan'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

def detailparam(request,id):
    param = ParameterData.objects.get(pk=id)
    return render(request,'report/parameter/dtl_param.html',{'param':param})


    
class list_param_dua(View):
    context = {'segment': 'param'}

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

        return render(request, template, context)
    
    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('d-param')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        param = self.get_object(pk)
        param.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Data Berhasil Di Hapus')
            redirect_url = reverse('d-param')

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
                        filter_params = Q(products__nama_produk__icontains=key.strip())
                    else:
                        filter_params |= Q(products__nama_produk__icontains=key.strip())

        param = ParameterData.objects.filter(filter_params) if filter_params else ParameterData.objects.filter(j_vendor=2).order_by('-id')
        self.context['param'], self.context['info'] = set_pagination(request, param)
        if not self.context['param']:
            return False, self.context['info']

        return self.context, 'report/parameter/data_parameter2.html'

    def edit(self, request, pk):
        param = self.get_object(pk)

        self.context['param'] = param
        self.context['form'] = FSForm(instance=param)

        return self.context, 'report/parameter/edit_parameter.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        produk = self.get_object(pk)
        form = ParamForm(instance=produk)
        context = {'instance': produk, 'form': form}
        return render_to_string('report/parameter/edit_parameter_row.html', context)

    """ Common methods """
        
    def get_object(self, pk):
        param = get_object_or_404(ParameterData, id=pk)
        return param
    
    def get_row_item(self, pk):
        pengiriman = self.get_object(pk)
        edit_row = render_to_string('report/parameter/edit_parameter_row.html', {'instance': pengiriman})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = ParamForm(form_data, instance=transaction)        
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Parameter Data Berhasil DiSimpan')

            return True, 'Parameter Data Berhasil DiSimpan'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

