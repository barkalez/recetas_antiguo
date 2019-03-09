from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='recetas-home'),
    path('about/', views.about, name='recetas-about'),
]
