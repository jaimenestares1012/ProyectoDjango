from django.views.generic.base import TemplateView
from aplications.departamento.models import Departamento
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView)
# Create your views here.


from .models import Empleado, Habilidades


class ListaAllEmpleado(ListView):
    template_name='persona/lista_all.html'
    paginate_by= 4
    model=Empleado


class ListaByEmpleado(ListView):
    template_name='persona/lista_by.html'
    queryset=Empleado.objects.filter(
    ) 
    def get_queryset(self):
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista
class ListEmpleadosByKbord(ListView):
    template_name='persona/by_kword.html'
    context_object_name='empleados'
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", )
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        ) 
        return lista

class ListHabilidadesEmpleados(ListView):
    template_name="persona/habilidades.html"
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=self.request.GET.get("habilidad", )
        lista=Empleado.objects.filter(
            first_name=empleado
        ) 
        return []

class EmpleadoDetailView(DetailView):
    model=Empleado
    template_name="persona/detalle_persona.html"

    def get_context_data(self, **kwargs):
        context= super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

class sucessView(TemplateView):
    template_name="persona/sucess.html"

class CreateEmpleado(CreateView):
     template_name="persona/create.html"
     model=Empleado
     fields=('__all__')
     success_url=reverse_lazy('persona_app:sucesion')

