from django.urls import path, re_path
from apps.paramvendor import views as v_views

urlpatterns = [
    path('ajax_gst/',v_views.gastiasih_origin, name='h-gasti-origin'),##Add Commodiy
]
