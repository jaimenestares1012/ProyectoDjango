from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

#################### impotamos el modelo para trabjar con ellas en el template

from .models import Prueba
# Create your views here.
class PruebaView(TemplateView):
    template_name='home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name='listaNumeros'
    queryset=['1', '10', '20']

class ListarPrueba(ListView):
    template_name="home/nuevo.html"
    model=Prueba
    context_object_name="lista"    


class PruebaCreateView(CreateView):

    template_name = "home/add.html"
    model=Prueba
    fields=['titulo', 'subtitulo', 'cantidad']
