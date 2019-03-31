from django.urls import path
from .views import (
    RecetasListView,
    RecetasDetailView,
    RecetasCreateView,
    RecetasUpdateView,
    RecetasDeleteView
)
from . import views

urlpatterns =[
    path('', RecetasListView.as_view(), name='recetas-home'),
    path('recetas/<int:pk>', RecetasDetailView.as_view(), name='recetas-detail'),
    path('recetas/new', RecetasCreateView.as_view(), name='recetas-create'),
    path('recetas/<int:pk>/update', RecetasUpdateView.as_view(), name='recetas-update'),
    path('recetas/<int:pk>/delete', RecetasDeleteView.as_view(), name='recetas-delete'),
    path('about/', views.about, name='recetas-about'),
]
