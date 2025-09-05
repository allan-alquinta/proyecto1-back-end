from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.HomeView.as_view(), name='home'),

    # ---- Clientes ----
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # ---- Tarifas ----
    path('tarifas/', views.TarifaListView.as_view(), name='tarifa_list'),
    path('tarifas/nueva/', views.TarifaCreateView.as_view(), name='tarifa_create'),
    path('tarifas/<int:pk>/editar/', views.TarifaUpdateView.as_view(), name='tarifa_update'),
    path('tarifas/<int:pk>/eliminar/', views.TarifaDeleteView.as_view(), name='tarifa_delete'),

    # ---- Contratos ----
    path('contratos/', views.ContratoListView.as_view(), name='contrato_list'),
    path('contratos/nuevo/', views.ContratoCreateView.as_view(), name='contrato_create'),
    path('contratos/<int:pk>/editar/', views.ContratoUpdateView.as_view(), name='contrato_update'),
    path('contratos/<int:pk>/eliminar/', views.ContratoDeleteView.as_view(), name='contrato_delete'),

    # ---- Medidores ----
    path('medidores/', views.MedidorListView.as_view(), name='medidor_list'),
    path('medidores/nuevo/', views.MedidorCreateView.as_view(), name='medidor_create'),
    path('medidores/<int:pk>/editar/', views.MedidorUpdateView.as_view(), name='medidor_update'),
    path('medidores/<int:pk>/eliminar/', views.MedidorDeleteView.as_view(), name='medidor_delete'),
]
