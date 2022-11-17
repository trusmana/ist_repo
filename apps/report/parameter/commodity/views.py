from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.views import View
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse,QueryDict
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from apps.utils import set_pagination
from apps.products.models import Commodity
from apps.report.parameter.commodity.forms import CommodityForm

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class list_commodity(View):
    context = {'segment': 'commodity'}

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
        return redirect('d-commodity')

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
            redirect_url = reverse('d-commodity')

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

        commodity = Commodity.objects.filter(filter_params) if filter_params else Commodity.objects.filter(status=1).order_by('-id')

        self.context['commodity'], self.context['info'] = set_pagination(request, commodity)
        if not self.context['commodity']:
            return False, self.context['info']

        return self.context, 'report/commodity/data_commodity.html'

    def edit(self, request, pk):
        commodity = self.get_object(pk)

        self.context['commodity'] = commodity
        self.context['form'] = CommodityForm(instance=commodity)

        return self.context, 'report/commodity/edit_commodity.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        commodity = self.get_object(pk)
        form = CommodityForm(instance=commodity)
        context = {'instance': commodity, 'form': form}
        return render_to_string('report/commodity/edit_commodity_row.html', context)

    """ Common methods """
        
    def get_object(self, pk):
        commodity = get_object_or_404(Commodity, id=pk)
        return commodity
    
    def get_row_item(self, pk):
        commodity = self.get_object(pk)
        edit_row = render_to_string('report/commodity/edit_commodity_row.html', {'instance': commodity})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = CommodityForm(form_data, instance=transaction)        
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Commodity Berhasil DiSimpan')

            return True, 'Commodity Berhasil DiSimpan'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'
    
@login_required(login_url=settings.LOGIN_URL)
#@user_passes_test(lambda u: u.groups.filter(name__in=('Administrator','Admin_IT')))
def addcommodity(request):
    user = request.user
    if request.method == 'POST':
        form = CommodityForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.cu = user
            prod.save()
            messages.success(request, 'Data Commodity Berhasil Di Input')
            return redirect('d-commodity')
    else:
        form = CommodityForm(initial={'status':1})
    return render(request,'report/commodity/add_commodity.html',{'form':form})