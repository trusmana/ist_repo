from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
import io,xlsxwriter
from apps.products.models import Job,Sale
from apps.report.job.forms import DateForm

@login_required(login_url=settings.LOGIN_URL)
def report_job(request):
    data = Job.objects.filter(status_job = None)
    form = DateForm()
    if ('from_date' in request.GET) and ('until_date' in request.GET) and ('report' in request.GET) :
        from_date =request.GET['from_date']
        until_date = request.GET['until_date']
        report = request.GET['report']
        if (report) == '1' :
            data = Job.objects.filter(tanggal_invoice__range=(from_date,until_date),status_job=None)
            print('view dong')
        else:
            data = Job.objects.filter(tanggal_invoice__range=(from_date,until_date),status_job=None)
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': 0, 'fg_color': '#D7E4BC'})
            money_format = workbook.add_format({'num_format': '#,###.#0'})
            date_format = workbook.add_format({'num_format': 'dd-mm-yyyy'})
            merge_format = workbook.add_format({'bold': 1,'border': 6,'align': 'center','valign': 'vcenter','fg_color': '#D7E4BC'})
            
            worksheet.set_column(0, 0, 6)
            worksheet.set_column(1, 1, 18)
            worksheet.set_column(2, 2, 10)
            
            worksheet.merge_range('A1:O1', 'Data Pekerjaan PT Indah Sinergi Treding (Done)', merge_format)  # type: ignore
            worksheet.write('A4:A4', 'NO', bold)
            worksheet.write('B4:B4', 'Tanggal Pekerjaan', bold)
            worksheet.write('C4:C4', 'Nomor Pekerjaan', bold)
            worksheet.write('D4:D4', 'Vendor', bold)
            worksheet.write('E4:E4', 'Comoodity', bold)
            worksheet.write('F4:F4', 'Invoce', bold)
            worksheet.write('G4:G4', 'Invoce 1', bold)
            worksheet.write('H4:H4', 'Invoce 2', bold)
            worksheet.write('I4:I4', 'AirFreigh', bold)
            worksheet.write('J4:J4', 'Handling Charges', bold)
            worksheet.write('K4:K4', 'Incurance', bold)
            worksheet.write('L4:L4', 'Fuel Surcharge', bold)
            worksheet.write('M4:M4', 'Import Handling Charges', bold)
            worksheet.write('N4:N4', 'GST Zero Rate', bold)
            worksheet.write('O4:O4', 'Storage At Cosh', bold)    
            row = 4
            col = 0
            nomor = 0
            
            for t in data:
                nomor +=1
                worksheet.write_number(row, col , nomor )
                worksheet.write_datetime(row, col + 1 , t.tanggal_invoice,date_format)
                worksheet.write_number(row, col + 2 , t.transaksi.no_pekerjaan)
                worksheet.write_string(row, col + 3 , t.vendor.nama_jasa_pengiriman)
                worksheet.write_string(row, col + 4 , t.transaksi.commodity.nama ) # type: ignore
                worksheet.write_string(row, col + 5 , t.no_invoice )
                if t.no_invoice_sl_2:
                    worksheet.write_string(row, col + 6 , t.no_invoice_sl_2 )
                else:
                    worksheet.write_string(row, col + 6 , '')
                if t.no_invoice_sl_3:    
                    worksheet.write_string(row, col + 7 , t.no_invoice_sl_3 )
                else:
                    worksheet.write_string(row, col + 7 , '' )
                worksheet.write_number(row, col + 8 , t.airfreight,money_format )
                worksheet.write_number(row, col + 9 , t.handling_charges,money_format )
                worksheet.write_number(row, col + 10 , t.insurance_security_surcharge,money_format )
                worksheet.write_number(row, col + 11 , t.fuel_surcharge,money_format )
                worksheet.write_number(row, col + 12 , t.import_handling_charges,money_format )
                worksheet.write_number(row, col + 13 , t.gst_zero_rated,money_format )
                worksheet.write_number(row, col + 14 , t.storage_at_cost,money_format )    
                row += 1
            
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename=DataJob_%s_SAMPAI_%s.xlsx" % (from_date,until_date)
            return response

    form = DateForm()
    return render(request,'job/reportjob/report_job.html',{'data':data,'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def report_job_done(request):
    data = Job.objects.filter(status_job = 1)
    form = DateForm()
    if ('from_date' in request.GET) and ('until_date' in request.GET) and ('report' in request.GET) :
        from_date =request.GET['from_date']
        until_date = request.GET['until_date']
        report = request.GET['report']
        if (report) == '1' :
            data = Job.objects.filter(tanggal_invoice__range=(from_date,until_date),status_job=1)
            print('view dong')
        else:
            data = Job.objects.filter(tanggal_invoice__range=(from_date,until_date),status_job=1)
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': 0, 'fg_color': '#D7E4BC'})
            money_format = workbook.add_format({'num_format': '#,###.#0'})
            date_format = workbook.add_format({'num_format': 'dd-mm-yyyy'})
            merge_format = workbook.add_format({'bold': 1,'border': 6,'align': 'center','valign': 'vcenter','fg_color': '#D7E4BC'})
            
            worksheet.set_column(0, 0, 6)
            worksheet.set_column(1, 1, 18)
            worksheet.set_column(2, 2, 10)
            
            worksheet.merge_range('A1:O1', 'Data Pekerjaan PT Indah Sinergi Treding', merge_format)  # type: ignore
            worksheet.write('A4:A4', 'NO', bold)
            worksheet.write('B4:B4', 'Tanggal Pekerjaan', bold)
            worksheet.write('C4:C4', 'Nomor Pekerjaan', bold)
            worksheet.write('D4:D4', 'Vendor', bold)
            worksheet.write('E4:E4', 'Comoodity', bold)
            worksheet.write('F4:F4', 'Invoce', bold)
            worksheet.write('G4:G4', 'Invoce 1', bold)
            worksheet.write('H4:H4', 'Invoce 2', bold)
            worksheet.write('I4:I4', 'AirFreigh', bold)
            worksheet.write('J4:J4', 'Handling Charges', bold)
            worksheet.write('K4:K4', 'Incurance', bold)
            worksheet.write('L4:L4', 'Fuel Surcharge', bold)
            worksheet.write('M4:M4', 'Import Handling Charges', bold)
            worksheet.write('N4:N4', 'GST Zero Rate', bold)
            worksheet.write('O4:O4', 'Storage At Cosh', bold)    
            row = 4
            col = 0
            nomor = 0
            
            for t in data:
                nomor +=1
                worksheet.write_number(row, col , nomor )
                worksheet.write_datetime(row, col + 1 , t.tanggal_invoice,date_format)
                worksheet.write_number(row, col + 2 , t.transaksi.no_pekerjaan)
                worksheet.write_string(row, col + 3 , t.vendor.nama_jasa_pengiriman)
                worksheet.write_string(row, col + 4 , t.transaksi.commodity.nama )# type: ignore
                worksheet.write_string(row, col + 5 , t.no_invoice )
                if t.no_invoice_sl_2:
                    worksheet.write_string(row, col + 6 , t.no_invoice_sl_2 )
                else:
                    worksheet.write_string(row, col + 6 , '')
                if t.no_invoice_sl_3:    
                    worksheet.write_string(row, col + 7 , t.no_invoice_sl_3 )
                else:
                    worksheet.write_string(row, col + 7 , '' )
                worksheet.write_number(row, col + 8 , t.airfreight,money_format )
                worksheet.write_number(row, col + 9 , t.handling_charges,money_format )
                worksheet.write_number(row, col + 10 , t.insurance_security_surcharge,money_format )
                worksheet.write_number(row, col + 11 , t.fuel_surcharge,money_format )
                worksheet.write_number(row, col + 12 , t.import_handling_charges,money_format )
                worksheet.write_number(row, col + 13 , t.gst_zero_rated,money_format )
                worksheet.write_number(row, col + 14 , t.storage_at_cost,money_format )    
                row += 1
            
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename=DataJobDone_%s_SAMPAI_%s.xlsx" % (from_date,until_date)
            return response
    form = DateForm()
    return render(request,'job/reportjob/report_job_done.html',{'data':data,'forms':form})