from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.views import View
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse,QueryDict
from django.template.loader import render_to_string
from django.urls import reverse
import datetime
from django.conf import settings
from apps.utils import set_pagination

from apps.report.parameter.paramdata2.forms import ParamDuaForm
from apps.products.models import ParameterDataBl



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class list_param2(View):
    context = {'segment': 'param2'}

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
        return redirect('d-paramjl')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        negara = self.get_object(pk)
        negara.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Data Berhasil Di Hapus')
            redirect_url = reverse('d-paramjl')

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
                        filter_params = Q(nama_negara__icontains=key.strip())
                    else:
                        filter_params |= Q(nama_negara__icontains=key.strip())

        pengiriman = ParameterDataBl.objects.filter(filter_params) if filter_params else ParameterDataBl.objects.all().order_by('-id')

        self.context['param2'], self.context['info'] = set_pagination(request, pengiriman)
        if not self.context['param2']:
            return False, self.context['info']

        return self.context, 'report/parameter2/data_parameter2.html'

    def edit(self, request, pk):
        pengiriman = self.get_object(pk)

        self.context['param2'] = pengiriman
        self.context['form'] = ParamDuaForm(instance=pengiriman)

        return self.context, 'report/parameter2/edit_parameter.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        negara = self.get_object(pk)
        form = ParamDuaForm(instance=negara)
        context = {'instance': negara, 'form': form}
        return render_to_string('report/parameter2/edit_parameter_row.html', context)

    """ Common methods """
        
    def get_object(self, pk):
        negara = get_object_or_404(ParameterDataBl, id=pk)
        return negara
    
    def get_row_item(self, pk):
        negara = self.get_object(pk)
        edit_row = render_to_string('report/parameter2/edit_parameter_row.html', {'instance': negara})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = ParamDuaForm(form_data, instance=transaction)        
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Negara Berhasil DiSimpan')

            return True, 'Negara Berhasil DiSimpan'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    
@login_required(login_url=settings.LOGIN_URL)
#@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT')))
def addparamdatabl(request):
    user = request.user
    if request.method == 'POST':
        form = ParamDuaForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.cu = user
            prod.save()
            messages.success(request, 'Data Negara Berhasil Di Input')
            return redirect('d-paramjl')
    else:
        form = ParamDuaForm(initial={'tgl_aktif_param':datetime.date.today()})
    return render(request,'report/parameter2/add_parameter2.html',{'form':form})