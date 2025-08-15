from django.contrib import admin
from django.urls import path, include
from ui.views import home_redirect
urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('billing/', include('billing.urls')),
    path('payments/', include('payments.urls')),
    path('vouchers/', include('vouchers.urls')),
    path('devices/', include('devices.urls')),
    path('ui/', include('ui.urls')),
]
