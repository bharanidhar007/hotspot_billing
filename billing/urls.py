from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='billing-dashboard'),
    path('stats/', views.dashboard_stats, name='billing-stats'),
    path('withdraw/<int:hotspot_id>/', views.request_withdrawal, name='request-withdrawal'),
    path('withdraw/approve/<int:wid>/', views.approve_withdrawal, name='approve-withdrawal'),
]
