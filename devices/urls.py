from django.urls import path
from . import views
urlpatterns = [
    path('mikrotik/', views.mikrotik, name='mikrotik'),
    path('equipment/', views.equipment, name='equipment'),
]
