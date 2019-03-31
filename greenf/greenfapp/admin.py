from django.contrib import admin
from .models import Recetas, Ingredientes, Tipo_cantidad


# Register your models here.
admin.site.register(Recetas)
admin.site.register(Ingredientes)
admin.site.register(Tipo_cantidad)
