from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




class  Tipo_cantidad(models.Model):
    tipo_cantidad = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tipo_cantidad

    class Meta:
        verbose_name_plural = 'Tipo_Cantidad'

class Ingredientes(models.Model):
    nombre = models.CharField(max_length=100,null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    tipo_cantidad = models.ForeignKey(Tipo_cantidad, on_delete=models.CASCADE)

    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        cadena = "{0} => {1} => {2}"
        return cadena.format(self.nombre, self.cantidad, self.tipo_cantidad)
    class Meta:
        verbose_name_plural = 'Ingredientes'

class Recetas(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingredientes)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('recetas-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Recetas'
