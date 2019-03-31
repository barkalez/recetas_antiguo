from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Recetas



def home(request):
    context = {
        'recetas': Recetas.objects.all()
    }
    return render(request, 'greenfapp/home.html', context)

class RecetasListView(ListView):
    model = Recetas
    template_name = 'greenfapp/home.html'
    context_object_name = 'recetas'
    ordering = ['-author']

class RecetasDetailView(DetailView):
    model = Recetas

class RecetasCreateView(LoginRequiredMixin, CreateView):
    model = Recetas
    fields = [
        'nombre',
        'ingredientes',
        'author'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecetasUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recetas
    fields = [
        'nombre',
        'ingredientes',
        'author'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recetas = self.get_object()
        if self.request.user == recetas.author:
            return True
        return False

class RecetasDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recetas
    success_url = '/'

    def test_func(self):
        recetas = self.get_object()
        if self.request.user == recetas.author:
            return True
        return False


def about(request):
    return render(request, 'greenfapp/about.html', {'title': 'About'})
