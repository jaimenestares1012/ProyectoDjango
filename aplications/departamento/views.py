from aplications import departamento
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
# Create your views here.
from .forms import NewDepartamentoForm
from .models import Departamento
from aplications.persona.models import Empleado
from django.urls import reverse_lazy

class NewDepartamento(FormView):
    template_name="departamento/new_dep.html"
    form_class=NewDepartamentoForm
    success_url=reverse_lazy('persona_app:inicio')
    

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


class ListarDepartamento(ListView):
    template_name="departamento/lista_departamento.html"
    model=Departamento
    paginate_by=5
    
    # def get_queryset(self):
    #     palabra_clave=self.request.GET.get("depa", '')
    #     lista=Empleado.objects.filter(
    #         first_name__icontains=palabra_clave
    #     )
    #     return lista
