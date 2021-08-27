from aplications import departamento
from django.shortcuts import render
from django.views.generic.edit import FormView
# Create your views here.
from .forms import NewDepartamentoForm
from .models import Departamento
from aplications.persona.models import Empleado
class NewDepartamento(FormView):
    template_name="departamento/new_dep.html"
    form_class=NewDepartamentoForm
    success_url='/'
    

    def form_valid(self,form):
        depa=Departamento(
        name= form.cleaned_data['departamento'],
        shor_name= form.cleaned_data['shorname']
        )
        depa.save()
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa   
        )
        
        return super(NewDepartamento, self).form_valid(form)
