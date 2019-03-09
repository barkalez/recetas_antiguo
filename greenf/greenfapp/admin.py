from django.contrib import admin
from .models import Recetas, Ingredientes, TipCant

# Register your models here.
admin.site.register(Recetas)
admin.site.register(Ingredientes)
admin.site.register(TipCant)
