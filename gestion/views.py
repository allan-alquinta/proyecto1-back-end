from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Tarifa, Contrato, Medidor

class HomeView(TemplateView):
    template_name = 'layout/home.html'

# ====== Clientes ======
class ClienteListView(ListView):
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# ====== Tarifas ======
class TarifaListView(ListView):
    model = Tarifa
    template_name = 'gestion/tarifa_list.html'
    context_object_name = 'tarifas'

class TarifaCreateView(CreateView):
    model = Tarifa
    fields = ['tipo_tarifa', 'precio', 'fecha_vigencia']
    template_name = 'gestion/tarifa_form.html'
    success_url = reverse_lazy('tarifa_list')

class TarifaUpdateView(UpdateView):
    model = Tarifa
    fields = ['tipo_tarifa', 'precio', 'fecha_vigencia']
    template_name = 'gestion/tarifa_form.html'
    success_url = reverse_lazy('tarifa_list')

class TarifaDeleteView(DeleteView):
    model = Tarifa
    template_name = 'gestion/tarifa_confirm_delete.html'
    success_url = reverse_lazy('tarifa_list')

# ====== Contratos ======
class ContratoListView(ListView):
    model = Contrato
    template_name = 'gestion/contrato_list.html'
    context_object_name = 'contratos'

class ContratoCreateView(CreateView):
    model = Contrato
    fields = ['cliente', 'numero_contrato', 'fecha_inicio', 'fecha_fin', 'tarifa']
    template_name = 'gestion/contrato_form.html'
    success_url = reverse_lazy('contrato_list')

class ContratoUpdateView(UpdateView):
    model = Contrato
    fields = ['cliente', 'numero_contrato', 'fecha_inicio', 'fecha_fin', 'tarifa']
    template_name = 'gestion/contrato_form.html'
    success_url = reverse_lazy('contrato_list')

class ContratoDeleteView(DeleteView):
    model = Contrato
    template_name = 'gestion/contrato_confirm_delete.html'
    success_url = reverse_lazy('contrato_list')

# ====== Medidores ======
class MedidorListView(ListView):
    model = Medidor
    template_name = 'gestion/medidor_list.html'
    context_object_name = 'medidores'

class MedidorCreateView(CreateView):
    model = Medidor
    fields = ['contrato', 'numero_medidor', 'ubicacion', 'estado_medidor']
    template_name = 'gestion/medidor_form.html'
    success_url = reverse_lazy('medidor_list')

class MedidorUpdateView(UpdateView):
    model = Medidor
    fields = ['contrato', 'numero_medidor', 'ubicacion', 'estado_medidor']
    template_name = 'gestion/medidor_form.html'
    success_url = reverse_lazy('medidor_list')

class MedidorDeleteView(DeleteView):
    model = Medidor
    template_name = 'gestion/medidor_confirm_delete.html'
    success_url = reverse_lazy('medidor_list')
