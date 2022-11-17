from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include,re_path
from apps.report import views as vreport

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.core.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path("", include("apps.keuangan.urls")),
    path("", include("apps.paramvendor.urls")),    
    path("report/", include("apps.report.urls")),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT}),
    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', vreport.list_matauang.as_view(),
            name='transactions'),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
