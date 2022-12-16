from django.contrib import admin
from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from .models import Commodity, Job, MataUang,Kurs, ParameterData,Produk,JasaPengiriman,Negara,ParameterDataBl, Sale, Transaksi,\
    Transaksi,Job,RefCustomer


class SaleAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id',]
    search_fields = ['id']
admin.site.register(Sale,SaleAdmin)

class RefCustomerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id',]
    search_fields = ['id']
admin.site.register(RefCustomer,RefCustomerAdmin)

class MataUangAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','status','nama_mata_uang',]
    search_fields = ['id']
admin.site.register(MataUang,MataUangAdmin)

class KursAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','status_kurs','tanggal_aktif']
    search_fields = ['id']
admin.site.register(Kurs,KursAdmin)

class ProdukAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','id_prod','nama_produk','tgl_aktif','status']
    search_fields = ['id']
admin.site.register(Produk,ProdukAdmin)

class JasaPengirimanAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','nama_jasa_pengiriman','status']
    search_fields = ['id']
admin.site.register(JasaPengiriman,JasaPengirimanAdmin)

class ParameterDataAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','products']
    search_fields = ['id']
admin.site.register(ParameterData,ParameterDataAdmin)

class ParameterDataBlAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','products']
    search_fields = ['id']
admin.site.register(ParameterDataBl,ParameterDataBlAdmin)

class TransaksiAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']
admin.site.register(Transaksi,TransaksiAdmin)

class JobAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','transaksi','vendor','no_invoice']
    search_fields = ['id','no_invoice']
admin.site.register(Job,JobAdmin)


class CommodityAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','nama','status']
    search_fields = ['id','no_invoice']
admin.site.register(Commodity,CommodityAdmin)

class NegaraAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','nama_negara']
    search_fields = ['id']
admin.site.register(Negara,NegaraAdmin)