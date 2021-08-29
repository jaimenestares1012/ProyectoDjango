from django.db import models
from aplications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
     habilidad = models.CharField('habilidad', max_length=50)
     class meta:
         verbose_name='Hablidad'
         verbose_name_plural='Habilidades empleados'
     def __str__(self):
         return str(self.id) + '-' + self.habilidad


# Create your models here.
class Empleado(models.Model):
    job_choices=(
        ('0', 'contador'),
        ('1', 'Administrado'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField("nombre", max_length=50)
    last_name = models.CharField("apellido", max_length=50)
    full_name = models.CharField("full_name", max_length=120, blank=True)
    job = models.CharField("Trabajo", max_length=50, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida= RichTextField()
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    class Meta:
        verbose_name='empleados'
        verbose_name_plural="Los empleados"
        ordering=['first_name']

    def __str__(self) :
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
        