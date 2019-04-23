from django.urls import path
from .views import (
    RecetasListView,
    RecetasDetailView,
    RecetasCreateView,
    RecetasUpdateView,
    RecetasDeleteView,
    IngredientesCreateView,
    CantidadCreateView,
    Tipo_cantidadCreateView

)
from . import views

urlpatterns =[
    path('', RecetasListView.as_view(), name='recetas-home'),
    path('recetas/<int:pk>', RecetasDetailView.as_view(), name='recetas-detail'),
    path('recetas/new', RecetasCreateView.as_view(), name='recetas-create'),
    path('ingredientes/new', IngredientesCreateView.as_view(), name='ingredientes-create'),
    path('cantidad/new', CantidadCreateView.as_view(), name='cantidad-create'),
    path('tip_cant/new', Tipo_cantidadCreateView.as_view(), name='tip_cant-create'),
    path('recetas/<int:pk>/update', RecetasUpdateView.as_view(), name='recetas-update'),
    path('recetas/<int:pk>/delete', RecetasDeleteView.as_view(), name='recetas-delete'),
    path('about/', views.about, name='recetas-about'),
]
