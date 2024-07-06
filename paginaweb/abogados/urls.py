from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

handler404 = custom_page_not_found_view





urlpatterns = [
    path('Inicio', views.Inicio, name='Inicio'),
    path('Registro', views.Registro, name='Registro'),
    path('Sobre_nosotros', views.Sobre_nosotros, name='Sobre_nosotros'),
    path('TecnicoJuridico', views.TecnicoJuridico, name='TecnicoJuridico'),
    path('VistaAbogadoAdministrador', views.VistaAbogadoAdministrador, name='VistaAbogadoAdministrador'),
    path('VistaAbogadoConsultor', views.VistaAbogadoConsultor, name='VistaAbogadoConsultor'),
    path('VistaCliente', views.VistaCliente, name='VistaCliente'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),  # Usa la vista personalizada para logout
    path('register_abogado/', views.register_abogado, name='register_abogado'),
    path('register_cliente/', views.register_cliente, name='register_cliente'),
    path('update_profile/', views.update_profile, name='update_profile'),
    # CRUD para los clientes
    path('', views.vista_cliente, name='vista_cliente'),
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('actualizar/<int:pk>/', views.actualizar_solicitud, name='actualizar_solicitud'),
    path('eliminar/<int:pk>/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('GenerarReporteFinanciero/', views.GenerarReporteFinanciero, name='GenerarReporteFinanciero'),
    path('generar_contrato/', views.GenerarContrato, name='generar_contrato'),
    path('carrusel/', views.carrusel_view, name='carrusel'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
