from django.urls import path
from . import views

urlpatterns = [
    # Home simple
    path('', views.HomeView.as_view(), name='home'),

    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),

    # Tarifas
    path('tarifas/', views.TarifaListView.as_view(), name='tarifa_list'),
    path('tarifas/nueva/', views.TarifaCreateView.as_view(), name='tarifa_create'),
]
