from django.db import models
from django.contrib.auth.models import User

class Ingredientes(models.Model):
    nombre = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nombre

class TipCant(models.Model):
    tipcant = models.CharField(max_length=15,null=True, blank=True)

    def __str__(self):
        return self.tipcant

class Recetas(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    plato = models.CharField(max_length=100, null=True, blank=True)
    elaboracion = models.TextField(null=True, blank=True)

    ingrediente_1 = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created1a')
    cantidad_Ing_1 = models.IntegerField(null=True, blank=True)
    tipo_Cant_Ing_1 = models.ForeignKey(TipCant, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created1b')

    ingrediente_2 = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created2a')
    cantidad_Ing_2 = models.IntegerField(null=True, blank=True)
    tipo_Cant_Ing_2 = models.ForeignKey(TipCant, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created2b')

    ingrediente_3 = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created3a')
    cantidad_Ing_3 = models.IntegerField(null=True, blank=True)
    tipo_Cant_Ing_3 = models.ForeignKey(TipCant, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created3b')

    ingrediente_4 = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created4a')
    cantidad_Ing_4 = models.IntegerField(null=True, blank=True)
    tipo_Cant_Ing_4 = models.ForeignKey(TipCant, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_requests_created4b')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
