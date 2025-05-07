

from django.urls import path
from . import views

urlpatterns = [
    path('finance/', views.finance_home, name='finance_home'),
    path('investment/', views.investment, name='investment'),
    path('bond/', views.bond, name='bond'),
   
]