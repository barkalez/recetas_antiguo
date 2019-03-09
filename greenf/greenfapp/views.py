from django.shortcuts import render
from django.http import HttpResponse
from .models import Recetas



def home(request):
    context = {
        'recetas': Recetas.objects.all()
    }
    return render(request, 'greenfapp/home.html', context)

def about(request):
    return render(request, 'greenfapp/about.html', {'title': 'About'})
