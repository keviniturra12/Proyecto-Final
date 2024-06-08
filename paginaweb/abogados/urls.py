from django.urls import path
from . import views

urlpatterns = [
path('inicio',views.inicio, name='inicio'),
path('Formulario',views.Formulario, name='Formulario'),
path('Sobre_nosotros',views.Sobre_nosotros, name='Sobre_nosotros'),



]