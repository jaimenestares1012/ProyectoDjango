
from django.contrib import admin
from django.urls import path

from . import views
app_name = "persona_app"
urlpatterns = [
    path('listar_empleados/', views.ListaAllEmpleado.as_view()),
    path('listar_em/<shorname>', views.ListaByEmpleado.as_view()),
    path('buscar_empleado/', views.ListEmpleadosByKbord.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path('detalle_personas/<pk>/', views.EmpleadoDetailView.as_view()),
    path('create/', views.CreateEmpleado.as_view()),
    path('sucess/', views.sucessView.as_view(), name="sucesion"),

]