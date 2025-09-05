from django.contrib import admin
from .models import Cliente, Tarifa, Contrato, Medidor, Lectura, Boleta, Pago, Notificacion

admin.site.register(Cliente)
admin.site.register(Tarifa)
admin.site.register(Contrato)
admin.site.register(Medidor)
admin.site.register(Lectura)
admin.site.register(Boleta)
admin.site.register(Pago)
admin.site.register(Notificacion)
