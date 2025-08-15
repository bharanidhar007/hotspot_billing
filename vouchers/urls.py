from django.urls import path
from . import views
urlpatterns = [
    path('<int:hotspot_id>/', views.voucher_list, name='voucher-list'),
    path('<int:hotspot_id>/export/csv/', views.export_vouchers_csv, name='voucher-export-csv'),
    path('<int:hotspot_id>/export/pdf/', views.export_vouchers_pdf, name='voucher-export-pdf'),
]
