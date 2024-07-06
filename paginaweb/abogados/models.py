from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    rut_cliente = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Abogado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rut_abogado = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255, default='default@example.com')
    direccion = models.CharField(max_length=255, default='Dirección por defecto')
    telefono = models.CharField(max_length=255, default='123456789')
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class TecnicoJuridico(models.Model):
    rut_tecnico = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo_electronico = models.EmailField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_contrato = models.DateField()
    monto_contrato = models.DecimalField(max_digits=10, decimal_places=2)
    modalidad_pago = models.CharField(max_length=255)
    observacion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Contrato {self.id_contrato}"

class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nom_documento = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nom_documento


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.id_pago}"

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateField()
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificación {self.id_notificacion}"


class SolicitudServicio(models.Model):
    ESTADO_CHOICES =[
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
    ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_servicio = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    archivo_adjunto = models.FileField(upload_to='archivos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')
    abogado = models.ForeignKey(Abogado, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

#python manage.py makemigrations
#python manage.py migrate
