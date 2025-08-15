from django.urls import path
from . import views
urlpatterns = [
    path('webhook/<str:provider>/', views.mobile_money_webhook, name='mm-webhook'),
]
