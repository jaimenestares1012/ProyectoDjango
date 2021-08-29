
from django.contrib import admin
from django.urls import path

from . import views
app_name = "persona_app"
urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),
    path('listar_empleados/', views.ListaAllEmpleado.as_view(), name="empleados_all"),
    path('listar_em/<shorname>', views.ListaByEmpleado.as_view()),
    path('buscar_empleado/', views.ListEmpleadosByKbord.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path('detalle_personas/<pk>/', views.EmpleadoDetailView.as_view(),name='detalle_empleado'),
    path('create/', views.CreateEmpleado.as_view()),
    path('sucess/', views.sucessView.as_view(), name="sucesion"),
    path('update/<pk>', views.EmpleadoUpdateView.as_view(), name="modificar"),
    path('delete/<pk>', views.delete.as_view(), name="eliminar"),

]