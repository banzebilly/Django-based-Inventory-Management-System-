from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name='view_all'),
    path('add/', views.capture_shoes, name='capture_shoes'),
    path('restock/', views.re_stock, name='re_stock'),
    path('search/', views.search_shoe, name='search_shoe'),
    path('value/', views.value_per_item, name='value_per_item'),
    path('highest/', views.highest_qty, name='highest_qty'),
]
