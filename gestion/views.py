from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Tarifa

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
