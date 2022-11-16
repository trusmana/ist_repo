from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from weasyprint import HTML

from apps.products.models import Job,Sale

@login_required(login_url=settings.LOGIN_URL)
def debit_note(request,id):
    spk = Job.objects.get(id=id)
    html_string = render_to_string('report/cetak/debit_note.html', {'p': spk})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="DEBET_NOTE.pdf"'
        return response
    

@login_required(login_url=settings.LOGIN_URL)
#####cetak Sale IST
def invoice(request,id):
    ist = Sale.objects.get(id=id)
    html_string = render_to_string('report/cetak/invoice.html', {'data': ist})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="INVOICE.pdf"'
        return response
    