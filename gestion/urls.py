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

    # ---- Lecturas ----
    path('lecturas/', views.LecturaListView.as_view(), name='lectura_list'),
    path('lecturas/nueva/', views.LecturaCreateView.as_view(), name='lectura_create'),
    path('lecturas/<int:pk>/editar/', views.LecturaUpdateView.as_view(), name='lectura_update'),
    path('lecturas/<int:pk>/eliminar/', views.LecturaDeleteView.as_view(), name='lectura_delete'),

    # ---- Boletas ----
    path('boletas/', views.BoletaListView.as_view(), name='boleta_list'),
    path('boletas/nueva/', views.BoletaCreateView.as_view(), name='boleta_create'),
    path('boletas/<int:pk>/editar/', views.BoletaUpdateView.as_view(), name='boleta_update'),
    path('boletas/<int:pk>/eliminar/', views.BoletaDeleteView.as_view(), name='boleta_delete'),

    # ---- Pagos ----
    path('pagos/', views.PagoListView.as_view(), name='pago_list'),
    path('pagos/nuevo/', views.PagoCreateView.as_view(), name='pago_create'),
    path('pagos/<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('pagos/<int:pk>/eliminar/', views.PagoDeleteView.as_view(), name='pago_delete'),

    # ---- Notificaciones ----
    path('notificaciones/', views.NotificacionListView.as_view(), name='notificacion_list'),
    path('notificaciones/nueva/', views.NotificacionCreateView.as_view(), name='notificacion_create'),
    path('notificaciones/<int:pk>/editar/', views.NotificacionUpdateView.as_view(), name='notificacion_update'),
    path('notificaciones/<int:pk>/eliminar/', views.NotificacionDeleteView.as_view(), name='notificacion_delete'),
]
