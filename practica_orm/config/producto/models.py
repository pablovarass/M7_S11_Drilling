from django.db import models
import datetime

# Create your models here.

class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre  


class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    # fabrica = models.OneToOneField(Fabrica, on_delete=models.CASCADE, blank=True, null= True)
    # fabrica = models.ManyToManyField(Fabrica)

    def costo(self, obj):
        return "Costo Alto" if obj.precio >= 5000 else "Costo Bajo"
    costo.short_description = 'Costo'
