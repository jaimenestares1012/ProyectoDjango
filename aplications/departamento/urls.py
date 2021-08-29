
from django.contrib import admin
from django.urls import path


from . import views
app_name = "departamento_app"

urlpatterns = [
    path('new_departamento/', views.NewDepartamento.as_view(), name ='nuevo_depa'),
    path('Lista_departamento/', views.ListarDepartamento.as_view(), name ='lista_departamento'),


]
