from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from aplications.departamento.models import Departamento
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.


from .models import Empleado, Habilidades
class InicioView(TemplateView):
    template_name="inicio.html"

class ListaAllEmpleado(ListView):
    template_name='persona/lista_all.html'
    paginate_by= 5
    
    def get_queryset(self):
        palabra_clave=self.request.GET.get("Kword", '')
        lista=Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista


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
###datos de los empleados
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
     fields=[
         'first_name',
         'last_name',
         'job',
         'departamento',
         'habilidades'
     ]
     success_url=reverse_lazy('persona_app:sucesion')

     def form_valid(self, form):
         ##logica del proceso
         empleado=form.save()
         empleado.full_name=empleado.first_name + '' + empleado.last_name
         empleado.save()
         return super(CreateEmpleado, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name="persona/update.html"

    model=Empleado
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url=reverse_lazy('persona_app:sucesion')
    def post(self, request, *args, **kwargs) :
        self.object=self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form) :
        return super(EmpleadoUpdateView,self).form_valid(form)


class delete(DeleteView):
    model=Empleado
    template_name="persona/delete.html"
    success_url=reverse_lazy('persona_app:sucesion')
