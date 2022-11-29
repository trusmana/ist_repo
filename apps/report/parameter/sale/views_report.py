from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import datetime,io,xlsxwriter
from apps.products.models import Sale
from apps.report.job.forms import DateForm

@login_required(login_url=settings.LOGIN_URL)  # type: ignore
def report_sale(request):
    data = Sale.objects.filter(status_sale = None)
    form = DateForm()
    if ('from_date' in request.GET) and ('until_date' in request.GET) and ('report' in request.GET) :
        from_date =request.GET['from_date']
        until_date = request.GET['until_date']
        report = request.GET['report']
        if (report) == '1' :
            data = Sale.objects.filter(cdate__range=(from_date,until_date),status_sale=None)
            print('view dong')
        else:
            data = Sale.objects.filter(cdate__range=(from_date,until_date),status_sale=None)
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
            
            worksheet.merge_range('A1:S1', 'Data Sale PT Indah Sinergi Treding', merge_format)  # type: ignore
            worksheet.write('A4:A4', 'NO', bold)
            worksheet.write('B4:B4', 'Tanggal Pekerjaan', bold)
            worksheet.write('C4:C4', 'Nomor Pekerjaan', bold)
            worksheet.write('D4:D4', 'Vendor', bold)
            worksheet.write('E4:E4', 'Comoodity', bold)
            worksheet.write('F4:F4', 'Cartage Warehouse Charge', bold)
            worksheet.write('G4:G4', 'Airfreight', bold)
            worksheet.write('H4:H4', 'Cartage Warehouse Charge', bold)
            worksheet.write('I4:I4', 'AirFreigh', bold)
            worksheet.write('J4:J4', 'Export Handling', bold)
            worksheet.write('K4:K4', 'Incurance', bold)
            worksheet.write('L4:L4', 'Freight', bold)
            worksheet.write('M4:M4', 'Doc clearance', bold)
            worksheet.write('N4:N4', 'Ground Handling', bold)
            worksheet.write('O4:O4', 'Warehouse Charge', bold)
            worksheet.write('P4:P4', 'Handling charge', bold)
            worksheet.write('Q4:Q4', 'Delivery', bold)
            worksheet.write('R4:R4', 'Duty Tax', bold)
            worksheet.write('S4:S4', 'Tax Handling Charge', bold)        
            row = 4
            col = 0
            nomor = 0
            
            for t in data:
                nomor +=1
                worksheet.write_number(row, col , nomor )
                worksheet.write_datetime(row, col + 1 , t.cdate,date_format)  # type: ignore
                worksheet.write_number(row, col + 2 , t.trans.no_pekerjaan) # type: ignore
                worksheet.write_string(row, col + 3 , t.prod.vendor.nama_jasa_pengiriman) # type: ignore
                worksheet.write_string(row, col + 4 , t.trans.commodity.nama ) # type: ignore
                worksheet.write_number(row, col + 5 , t.cartage_warehouse_charge_one,money_format )
                worksheet.write_number(row, col + 6 , t.airfreight_one,money_format )
                
                if t.cartage_warehouse_charge_two:
                    worksheet.write_number(row, col + 7 , t.cartage_warehouse_charge_two,money_format )
                else:
                    worksheet.write_string(row, col + 7 , '')
                if t.cartage_warehouse_charge_two:
                    worksheet.write_number(row, col + 8 , t.airfreight_two,money_format )
                else:
                    worksheet.write_string(row, col + 8 , '')
                worksheet.write_number(row, col + 9 , t.export_handling,money_format )
                worksheet.write_number(row, col + 10 , t.freight,money_format )
                worksheet.write_number(row, col + 11 , t.doc_clearance,money_format )
                worksheet.write_number(row, col + 12 , t.ground_handling,money_format )
                worksheet.write_number(row, col + 13 , t.warehouse_charge,money_format )
                worksheet.write_number(row, col + 14 , t.handling_charge,money_format )
                if t.delivery:
                    worksheet.write_number(row, col + 15 , t.delivery,money_format )
                else:
                    worksheet.write_string(row, col + 15 , '')
                if t.duty_tax:
                    worksheet.write_number(row, col + 16 , t.duty_tax,money_format )
                else:
                    worksheet.write_string(row, col + 16 , '')
                if t.tax_handling_charge:
                    worksheet.write_number(row, col + 17 , t.tax_handling_charge,money_format )
                else:
                    worksheet.write_string(row, col + 17 , '')        
                row += 1
            
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename=DataSALES_%s_SAMPAI_%s.xlsx" % (from_date,until_date)
            return response

    form = DateForm()
    return render(request,'report/sale/reportsale/report_sale.html',{'data':data,'forms':form})

@login_required(login_url=settings.LOGIN_URL)
def report_sale_done(request):
    data = Sale.objects.filter(status_sale = 1)
    form = DateForm()
    if ('from_date' in request.GET) and ('until_date' in request.GET) and ('report' in request.GET) :
        from_date =request.GET['from_date']
        until_date = request.GET['until_date']
        report = request.GET['report']
        if (report) == '1' :
            data = Sale.objects.filter(tanggal_invoice__range=(from_date,until_date),status_sale=1)
            print('view dong')
        else:
            data = Sale.objects.filter(tanggal_invoice__range=(from_date,until_date),status_sale=1)
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
            
            worksheet.merge_range('A1:S1', 'Data Sale PT Indah Sinergi Treding (Done)', merge_format)  # type: ignore
            worksheet.write('A4:A4', 'NO', bold)
            worksheet.write('B4:B4', 'Tanggal Pekerjaan', bold)
            worksheet.write('C4:C4', 'Nomor Pekerjaan', bold)
            worksheet.write('D4:D4', 'Vendor', bold)
            worksheet.write('E4:E4', 'Comoodity', bold)
            worksheet.write('F4:F4', 'Cartage Warehouse Charge', bold)
            worksheet.write('G4:G4', 'Airfreight', bold)
            worksheet.write('H4:H4', 'Cartage Warehouse Charge', bold)
            worksheet.write('I4:I4', 'AirFreigh', bold)
            worksheet.write('J4:J4', 'Export Handling', bold)
            worksheet.write('K4:K4', 'Incurance', bold)
            worksheet.write('L4:L4', 'Freight', bold)
            worksheet.write('M4:M4', 'Doc clearance', bold)
            worksheet.write('N4:N4', 'Ground Handling', bold)
            worksheet.write('O4:O4', 'Warehouse Charge', bold)
            worksheet.write('P4:P4', 'Handling charge', bold)
            worksheet.write('Q4:Q4', 'Delivery', bold)
            worksheet.write('R4:R4', 'Duty Tax', bold)
            worksheet.write('S4:S4', 'Tax Handling Charge', bold)    
            row = 4
            col = 0
            nomor = 0
            
            for t in data:
                nomor +=1
                worksheet.write_number(row, col , nomor )
                worksheet.write_datetime(row, col + 1 , t.cdate,date_format)  # type: ignore
                worksheet.write_number(row, col + 2 , t.trans.no_pekerjaan) # type: ignore
                worksheet.write_string(row, col + 3 , t.prod.vendor.nama_jasa_pengiriman) # type: ignore
                worksheet.write_string(row, col + 4 , t.trans.commodity.nama ) # type: ignore
                worksheet.write_number(row, col + 5 , t.cartage_warehouse_charge_one,money_format )
                worksheet.write_number(row, col + 6 , t.airfreight_one,money_format )
                
                if t.cartage_warehouse_charge_two:
                    worksheet.write_number(row, col + 7 , t.cartage_warehouse_charge_two,money_format )
                else:
                    worksheet.write_string(row, col + 7 , '')
                if t.cartage_warehouse_charge_two:
                    worksheet.write_number(row, col + 8 , t.airfreight_two,money_format )
                else:
                    worksheet.write_string(row, col + 8 , '')
                worksheet.write_number(row, col + 9 , t.export_handling,money_format )
                worksheet.write_number(row, col + 10 , t.freight,money_format )
                worksheet.write_number(row, col + 11 , t.doc_clearance,money_format )
                worksheet.write_number(row, col + 12 , t.ground_handling,money_format )
                worksheet.write_number(row, col + 13 , t.warehouse_charge,money_format )
                worksheet.write_number(row, col + 14 , t.handling_charge,money_format )
                if t.delivery:
                    worksheet.write_number(row, col + 15 , t.delivery,money_format )
                else:
                    worksheet.write_string(row, col + 15 , '')
                if t.duty_tax:
                    worksheet.write_number(row, col + 16 , t.duty_tax,money_format )
                else:
                    worksheet.write_string(row, col + 16 , '')
                if t.tax_handling_charge:
                    worksheet.write_number(row, col + 17 , t.tax_handling_charge,money_format )
                else:
                    worksheet.write_string(row, col + 17 , '')        
                row += 1
                row += 1
            
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename=DataJobDone_%s_SAMPAI_%s.xlsx" % (from_date,until_date)
            return response
    form = DateForm()
    return render(request,'report/sale/reportsale/report_sale.html',{'data':data,'forms':form})