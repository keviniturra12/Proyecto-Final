from django.contrib import admin
from .models import Cliente, Abogado, TecnicoJuridico, Contrato, Documento, Pago, Notificacion,SolicitudServicio


admin.site.register(Cliente)
admin.site.register(Abogado)
admin.site.register(TecnicoJuridico)
admin.site.register(Contrato)
admin.site.register(Documento)
admin.site.register(Pago)
admin.site.register(Notificacion)
admin.site.register(SolicitudServicio)
