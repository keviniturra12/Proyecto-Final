from django.urls import path
from . import views

urlpatterns = [
path('Inicio',views.Inicio, name='Inicio'),
path('Registro',views.Registro, name='Registro'),
path('Sobre_nosotros',views.Sobre_nosotros, name='Sobre_nosotros'),
path('TecnicoJuridico',views.TecnicoJuridico, name='TecnicoJuridico'),
path('VistaAbogadoAdministrador',views.VistaAbogadoAdministrador, name='VistaAbogadoAdministrador'),
path('VistaAbogadoConsultor',views.VistaAbogadoConsultor, name='VistaAbogadoConsultor'),
path('VistaCliente',views.VistaCliente, name='VistaCliente'),
path('carrusel/', views.carrusel_view, name='carrusel'),
]