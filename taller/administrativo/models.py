from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name='departamentos')

    def __str__(self):
        return f"Depto de {self.nombre_propietario} en {self.edificio.nombre}"
