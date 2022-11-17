from django.contrib import admin
from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from apps.keuangan.models import BiayaPusat,BiayaMapper,Tbl_Akun,Tbl_Transaksi

class Tbl_AkunAdmin(ImportExportMixin, ExportActionModelAdmin):
    list_display = ['id','coa','deskripsi']
    search_fields = ['id']
admin.site.register(Tbl_Akun, Tbl_AkunAdmin)

admin.site.register(BiayaPusat)
admin.site.register(BiayaMapper)
admin.site.register(Tbl_Transaksi)
