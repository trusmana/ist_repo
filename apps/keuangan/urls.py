from django.urls import path
from apps.keuangan import views as v
from apps.keuangan.pusat import views_gl as pst
from apps.keuangan.forms import Tbl_Transaksi_History_glForm

urlpatterns = [
    path('keuangan/gl_pst/',pst.gl_gl_pusat,{'form_class': Tbl_Transaksi_History_glForm},name='i-glpst'),
    path('keuangan/i_biaya/',v.input_gl,name='i-biaya'),
    path('del_jurnal/<int:id>/',v.hapus_jurnal,name='del-jurnal'),
]
