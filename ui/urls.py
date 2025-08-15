from django.urls import path
from . import views
urlpatterns = [
    path('users/active/', views.simple_page, {'title':'Active Users'}, name='active-users'),
    path('users/', views.simple_page, {'title':'Users'}, name='users'),
    path('tickets/', views.simple_page, {'title':'Tickets'}, name='tickets'),
    path('leads/', views.simple_page, {'title':'Leads'}, name='leads'),
    path('finance/packages/', views.simple_page, {'title':'Packages'}, name='packages'),
    path('finance/payments/', views.simple_page, {'title':'Payments'}, name='payments'),
    path('finance/vouchers/', views.simple_page, {'title':'Vouchers'}, name='vouchers'),
    path('finance/expenses/', views.simple_page, {'title':'Expenses'}, name='expenses'),
    path('comms/sms/', views.simple_page, {'title':'Sms'}, name='sms'),
    path('comms/emails/', views.simple_page, {'title':'Emails'}, name='emails'),
    path('comms/campaigns/', views.simple_page, {'title':'Campaigns'}, name='campaigns'),
]
