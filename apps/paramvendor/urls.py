from django.urls import path, re_path
from apps.paramvendor import views as v_views
from apps.paramvendor.invoice import views as inv_views
from apps.paramvendor.invoice import views_shipper as inv_shipper
from apps.paramvendor.invoice import term as terms
from apps.paramvendor.invoice import ddp as ddp
from apps.paramvendor.invoice import pic as pic
from apps.paramvendor.invoice import consigne as consigne
from apps.paramvendor.invoice import gabung_hsc as hsc

urlpatterns = [
    path('ajax_gst/',v_views.gastiasih_origin, name='h-gasti-origin'),##Add Commodiy
    path('add_invaddess/',inv_views.addinaddress, name='add-inv-address'),
    re_path(r'^list_address/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', inv_views.list_address.as_view(),
        name='list_address'),
    re_path(r'^list_shipper/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', inv_shipper.list_shiper.as_view(),
        name='list_shipper'),
    path('add_shipper/',inv_shipper.addshipper, name='add-shipper'),
    re_path(r'^list_term/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', terms.list_term.as_view(),
        name='list_term'),
    path('add_term/',terms.addterm, name='add-term'),
    re_path(r'^list_ddp/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', ddp.list_ddp.as_view(),
        name='list_ddp'),
    path('add_ddp/',ddp.addddp, name='add-ddp'),
    re_path(r'^list_pic/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', pic.list_pic.as_view(),
        name='list_pic'),
    path('add_pic/',pic.addpic, name='add-pic'),
    re_path(r'^list_consigne/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', consigne.list_consigne.as_view(),
        name='list_consigne'),
    path('add_consigne/',consigne.addconsigne, name='add-consigne'),   
    re_path(r'^list_hsc/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', hsc.list_hsc.as_view(),
        name='list_hsc'),
    path('add_hsc/',hsc.addhsc, name='add-hsc'),          
]
