from django.db import models

# -------------------
# Cliente
# -------------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


# -------------------
# Tarifa
# -------------------
class Tarifa(models.Model):
    tipo_tarifa = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vigencia = models.DateField()

    def __str__(self):
        return f"{self.tipo_tarifa} - ${self.precio}"


# -------------------
# Contrato
# -------------------
class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_contrato = models.CharField(max_length=20, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Contrato {self.numero_contrato} - {self.cliente.nombre}"


# -------------------
# Medidor
# -------------------
class Medidor(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    numero_medidor = models.CharField(max_length=30, unique=True)
    ubicacion = models.CharField(max_length=150)
    estado_medidor = models.CharField(max_length=50)

    def __str__(self):
        return f"Medidor {self.numero_medidor}"


# -------------------
# Lectura
# -------------------
class Lectura(models.Model):
    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE)
    fecha_lectura = models.DateField()
    lectura_actual = models.IntegerField()
    consumo_energetico = models.IntegerField()

    def __str__(self):
        return f"Lectura {self.fecha_lectura} - {self.medidor.numero_medidor}"


# -------------------
# Boleta
# -------------------
class Boleta(models.Model):
    lectura = models.ForeignKey(Lectura, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default="pendiente")

    def __str__(self):
        return f"Boleta {self.id} - {self.estado}"


# -------------------
# Pago
# -------------------
class Pago(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    fecha_pago = models.DateField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=50)
    numero_referencia = models.CharField(max_length=100, blank=True, null=True)
    estado_pago = models.CharField(max_length=50, default="pendiente")

    def __str__(self):
        return f"Pago {self.id} - {self.estado_pago}"


# -------------------
# Notificaciones (Lectura/Pago)
# -------------------
class Notificacion(models.Model):
    TIPO_CHOICES = (
        ("lectura", "Lectura"),
        ("pago", "Pago"),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación {self.tipo} - {self.fecha}"
