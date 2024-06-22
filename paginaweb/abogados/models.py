
from django.db import models
from django.contrib.auth.models import User #ESTE FROM ES PARA LAS CLASES DE PROYECTO LEX
# #Fue creado hoy 04-06-2024


#------------------------------------BASE DE DATOS ABOGADOS LEX --------------------------------------


#python manage.py makemigrations #primero migramos la tabla
#python manage.py migrate #luego lo migramos



class Cliente(models.Model):
     id_rut = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=255)
     apellido = models.CharField(max_length=255)
     correo_electronico = models.EmailField(max_length=255)
     direccion = models.CharField(max_length=255)
     telefono = models.CharField(max_length=255)
     fecha_nacimiento = models.DateField()
     clave = models.CharField(max_length=255)

     def __str__(self):
        return f"{self.nombre} {self.apellido}"
     
#---------------------------
class Abogado(models.Model):
     id_abogado = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=255)
     apellido = models.CharField(max_length=255)
     especialidad = models.CharField(max_length=255)
     ano_experiencia = models.IntegerField()
     cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)

     def __str__(self):
        return f"{self.nombre} {self.apellido}"
     #-----------------------------------------------------

class Contrato(models.Model):
     id_contrato = models.AutoField(primary_key=True)
     fecha_contrato = models.DateField()
     monto_contrato = models.DecimalField(max_digits=10, decimal_places=2)
     modalidad_pago = models.CharField(max_length=255)
     observacion = models.TextField()
     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

     def __str__(self):
        return f"Contrato {self.id_contrato}"
#------------------------------------
class Documento(models.Model):
     id_documento = models.AutoField(primary_key=True)
     nom_documento = models.CharField(max_length=255)
     tipo_documento = models.CharField(max_length=255)

     def __str__(self):
        return self.nom_documento

#-------------------------------------------------------
class Causa(models.Model):
     id_causas = models.AutoField(primary_key=True)
     titulo = models.CharField(max_length=255)
     tipo_causas = models.CharField(max_length=255)
     fecha_inicio = models.DateField()
     fecha_termino = models.DateField()
     estado = models.CharField(max_length=255)
     contrato = models.ForeignKey(Contrato, null=True, on_delete=models.SET_NULL)
     documento = models.ForeignKey(Documento, null=True, on_delete=models.SET_NULL)
     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Conectado a id_cliente
     descripcion_causas = models.TextField()

     def __str__(self):
        return self.titulo

    #---------------------

class EstadoCuenta(models.Model):
     id_estado_cuenta = models.AutoField(primary_key=True)
     fecha = models.DateField()
     ingresos = models.DecimalField(max_digits=10, decimal_places=2)
     gastos = models.DecimalField(max_digits=10, decimal_places=2)
     beneficio = models.DecimalField(max_digits=10, decimal_places=2)
     pago = models.ForeignKey('Pago', on_delete=models.CASCADE)

     def __str__(self):
        return f"Estado de Cuenta {self.id_estado_cuenta}"
   
#--------------------
class Pago(models.Model):
     id_pago = models.AutoField(primary_key=True)
     fecha_pago = models.DateField()
     monto = models.DecimalField(max_digits=10, decimal_places=2)
     tipo_pago = models.CharField(max_length=255)
     abogado = models.ForeignKey(Abogado, null=True, on_delete=models.SET_NULL)

     def __str__(self):
        return f"Pago {self.id_pago}"

#---------------------
class Notificacion(models.Model):
     id_notificacion = models.AutoField(primary_key=True)
     id_usuario = models.IntegerField()
     TIPO_USUARIO_CHOICES = [
         ('cliente', 'Cliente'),
         ('abogado', 'Abogado'),
     ]
     tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
     mensaje = models.TextField()
     fecha = models.DateField()
     leido = models.BooleanField(default=False)

#-----------DE AQUI ESTAS RELACIONES SE TIENEN QUE ANALIZAR PARA VER SU UTILIDAD --------------------------------------
#class Notificacion(models.Model):
 #   id_notificacion = models.AutoField(primary_key=True)
  #  mensaje = models.TextField()
   # fecha = models.DateField()
    #leido = models.BooleanField(default=False)

   # def __str__(self):
    #    return f"Notificación {self.id_notificacion}"     


#class Relation15(models.Model):
 #   notificacion = models.ForeignKey(Notificacion, on_delete=models.CASCADE)
  #  abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)

   # class Meta:
    #    unique_together = (('notificacion', 'abogado'),)

#class Relation3(models.Model):
 #   causa = models.ForeignKey(Causa, on_delete=models.CASCADE)
  #  abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)

   # class Meta:
    #    unique_together = (('causa', 'abogado'),)

#class Relation7(models.Model):
 #   cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  #  documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

   # class Meta:
    #    unique_together = (('cliente', 'documento'),)    
# forms.py

#-----------------------------------------------------------------

