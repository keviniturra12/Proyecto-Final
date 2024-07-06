from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from .models import Cliente, Abogado,SolicitudServicio, Pago
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import logout,authenticate, login
from django.core.files.storage import default_storage
from django.db.models import Sum
from django.db.models.functions import ExtractYear,ExtractMonth
import os
from django.conf import settings




def is_tecnico(user):
    return user.groups.filter(name='Tecnico_Juridico').exists()

def is_abogado_admin(user):
    return user.groups.filter(name='Abogado_Administrador').exists()
#def is_abogado_admin(user):
   # return user.is_authenticated and user.groups.filter(name='Abogados').exists() 


def is_abogado_consultor(user):
    return user.groups.filter(name='Abogado_Causas').exists()

def is_cliente(user):
    return user.groups.filter(name='Cliente').exists()

def Inicio(request):
    grupo_cliente = request.user.groups.filter(name='Cliente').exists() if request.user.is_authenticated else False
    grupo_tecnico = request.user.groups.filter(name='Tecnico_Juridico').exists() if request.user.is_authenticated else False
    grupo_abogado_causas = request.user.groups.filter(name='Abogado_Causas').exists() if request.user.is_authenticated else False
    grupo_abogado_admin = request.user.groups.filter(name='Abogado_Administrador').exists() if request.user.is_authenticated else False
    
    context = {
        'grupo_cliente': grupo_cliente,
        'grupo_tecnico': grupo_tecnico,
        'grupo_abogado_causas': grupo_abogado_causas,
        'grupo_abogado_admin': grupo_abogado_admin
    }
    return render(request, 'abogados/Inicio.html', context)

def carrusel_view(request):
    return render(request, 'abogados/carrusel.html')


def Registro(request):
    context={}
    return render(request,'abogados/Registro.html', context)

def Sobre_nosotros(request):
    grupo_cliente = request.user.groups.filter(name='Cliente').exists() if request.user.is_authenticated else False
    grupo_tecnico = request.user.groups.filter(name='Tecnico_Juridico').exists() if request.user.is_authenticated else False
    grupo_abogado_causas = request.user.groups.filter(name='Abogado_Causas').exists() if request.user.is_authenticated else False
    grupo_abogado_admin = request.user.groups.filter(name='Abogado_Administrador').exists() if request.user.is_authenticated else False
    
    context = {
        'grupo_cliente': grupo_cliente,
        'grupo_tecnico': grupo_tecnico,
        'grupo_abogado_causas': grupo_abogado_causas,
        'grupo_abogado_admin': grupo_abogado_admin
    }
    return render(request,'abogados/Sobre_nosotros.html', context)

@login_required
@user_passes_test(is_tecnico)
def TecnicoJuridico(request):
    causas_pendientes = SolicitudServicio.objects.filter(estado='Pendiente')
    causas_seguimiento = SolicitudServicio.objects.exclude(estado='Pendiente')
    abogados = Abogado.objects.all()

    grupo_cliente = request.user.groups.filter(name='Cliente').exists() if request.user.is_authenticated else False
    grupo_tecnico = request.user.groups.filter(name='Tecnico_Juridico').exists() if request.user.is_authenticated else False
    grupo_abogado_causas = request.user.groups.filter(name='Abogado_Causas').exists() if request.user.is_authenticated else False
    grupo_abogado_admin = request.user.groups.filter(name='Abogado_Administrador').exists() if request.user.is_authenticated else False

    if request.method == 'POST':
        if 'tipo_servicio' in request.POST:
            # Crear solicitud de servicio
            form = SolicitudServicioForm(request.POST, request.FILES)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.cliente = request.user
                solicitud.save()
                messages.success(request, 'Solicitud de servicio creada exitosamente.')
                return redirect('TecnicoJuridico')
            else:
                messages.error(request, 'Error en el formulario de solicitud de servicio.')

        elif 'tipo_ingreso' in request.POST:
            # Registrar un ingreso
            tipo_ingreso = request.POST['tipo_ingreso']
            monto_ingreso = request.POST['monto_ingreso']
            rut_asociado = request.POST['rut_asociado']
            fecha_registro = request.POST['fecha_registro']

            cliente = get_object_or_404(Cliente, rut_cliente=rut_asociado)

            Pago.objects.create(
                fecha_pago=fecha_registro,
                monto=monto_ingreso,
                tipo_pago=tipo_ingreso,
                cliente=cliente
            )

            messages.success(request, 'Ingreso registrado exitosamente.')
            return redirect('TecnicoJuridico')

        else:
            # Actualizar solicitud
            solicitud_id = request.POST.get('solicitud_id')
            abogado_rut = request.POST.get('abogado')
            archivo_presupuesto = request.FILES.get('archivo_presupuesto')
            solicitud = get_object_or_404(SolicitudServicio, pk=solicitud_id)

            try:
                abogado = Abogado.objects.get(rut_abogado=abogado_rut)
            except Abogado.DoesNotExist:
                messages.error(request, 'El abogado seleccionado no existe.')
                return redirect('TecnicoJuridico')

            # Asignar el abogado y subir el archivo
            solicitud.abogado = abogado
            if archivo_presupuesto:
                ruta_archivo = default_storage.save(os.path.join('archivos', archivo_presupuesto.name), archivo_presupuesto)
                solicitud.archivo_adjunto = ruta_archivo
            solicitud.estado = 'Aprobado'
            solicitud.save()

            messages.success(request, 'Solicitud actualizada y archivo subido exitosamente.')
            return redirect('TecnicoJuridico')

    else:
        form = SolicitudServicioForm()

    context = {
        'solicitudes': causas_pendientes,
        'causas_seguimiento': causas_seguimiento,
        'abogados': abogados,
        'grupo_cliente': grupo_cliente,
        'grupo_tecnico': grupo_tecnico,
        'grupo_abogado_causas': grupo_abogado_causas,
        'grupo_abogado_admin': grupo_abogado_admin,
        'form': form  # Pasando el formulario al contexto
    }

    return render(request, 'abogados/TecnicoJuridico.html', context)



@login_required
@user_passes_test(is_abogado_admin)
def VistaAbogadoAdministrador(request):
    causas_pendientes = SolicitudServicio.objects.filter(estado='Pendiente')
    causas_aprobadas = SolicitudServicio.objects.filter(estado='Aprobado')
    causas_completadas = SolicitudServicio.objects.filter(estado='Completado')
    years = Pago.objects.annotate(year=ExtractYear('fecha_pago')).values_list('year', flat=True).distinct()

    context = {
        'causas_pendientes': causas_pendientes,
        'causas_aprobadas': causas_aprobadas,
        'causas_completadas': causas_completadas,
        'years': years
    }

    return render(request, 'abogados/VistaAbogadoAdministrador.html', context)

@login_required
@user_passes_test(is_abogado_admin)
def GenerarReporteFinanciero(request):
    year = request.GET.get('year')

    pagos = Pago.objects.filter(fecha_pago__year=year) if year else Pago.objects.all()
    total_ingresos = pagos.aggregate(Sum('monto'))['monto__sum']

    pagos_por_mes = pagos.annotate(month=ExtractMonth('fecha_pago')).values('month').annotate(total=Sum('monto')).order_by('month')
    pagos_por_tipo = pagos.values('tipo_pago').annotate(total=Sum('monto')).order_by('tipo_pago')

    month_names = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }

    pagos_por_mes = [{'month_name': month_names[mes['month']], 'total': mes['total']} for mes in pagos_por_mes]

    context = {
        'total_ingresos': total_ingresos,
        'year': year,
        'pagos_por_mes': pagos_por_mes,
        'pagos_por_tipo': pagos_por_tipo
    }

    return render(request, 'abogados/ReporteFinanciero.html', context)


@login_required
@user_passes_test(is_abogado_admin)
def VerReporteFinanciero(request):
    return render(request, 'abogados/VerReporteFinanciero.html')


@login_required
@user_passes_test(is_abogado_consultor)
def VistaAbogadoConsultor(request):
    abogado = get_object_or_404(Abogado, user=request.user)
    causas_estudiar = SolicitudServicio.objects.filter(abogado=abogado, estado='Completado')
    causas_asignar = SolicitudServicio.objects.filter(abogado=abogado, estado='Aprobado')
    documentos = SolicitudServicio.objects.filter(abogado=abogado).exclude(archivo_adjunto='')
    clientes = Cliente.objects.all()  # Asegúrate de tener acceso a todos los clientes

    # Leer todos los archivos en la carpeta 'archivos'
    archivos = []
    archivos_dir = os.path.join(settings.MEDIA_ROOT, 'archivos')
    if os.path.exists(archivos_dir):
        for file_name in os.listdir(archivos_dir):
            archivos.append({
                'name': file_name,
                'url': default_storage.url('archivos/' + file_name)
            })

    if request.method == 'POST' and 'archivo_contrato' in request.FILES:
        solicitud_id = request.POST.get('solicitud_id')
        solicitud = get_object_or_404(SolicitudServicio, pk=solicitud_id)

        archivo_contrato = request.FILES['archivo_contrato']
        ruta_archivo = default_storage.save('archivos/' + archivo_contrato.name, archivo_contrato)
        solicitud.archivo_adjunto = ruta_archivo
        solicitud.estado = 'Completado'
        solicitud.save()
        return redirect('VistaAbogadoConsultor')

    context = {
        'causas_estudiar': causas_estudiar,
        'causas_asignar': causas_asignar,
        'documentos': documentos,
        'archivos': archivos,
        'clientes': clientes  # Pasando los clientes al contexto
    }
    return render(request, 'abogados/VistaAbogadoConsultor.html', context)

@login_required
@user_passes_test(is_abogado_consultor)
def GenerarContrato(request):
    if request.method == 'GET':
        rut_cliente = request.GET.get('rut_cliente')
        cliente = get_object_or_404(Cliente, rut_cliente=rut_cliente)

        context = {
            'cliente': cliente,
        }

        return render(request, 'abogados/Contrato.html', context)


@login_required
@user_passes_test(is_cliente)
def VistaCliente(request):
    cliente = Cliente.objects.get(user=request.user) 
    fecha_nacimiento_formateada = cliente.fecha_nacimiento.strftime('%d/%m/%Y')
    solicitudes = SolicitudServicio.objects.filter(cliente=request.user)

    grupo_cliente = request.user.groups.filter(name='Cliente').exists()
    grupo_tecnico = request.user.groups.filter(name='Tecnico_Juridico').exists()
    grupo_abogado_causas = request.user.groups.filter(name='Abogado_Causas').exists()
    grupo_abogado_admin = request.user.groups.filter(name='Abogado_Administrador').exists()

    context = {
        'rut': cliente.rut_cliente,
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
        'correo_electronico': cliente.correo_electronico,
        'telefono': cliente.telefono,
        'direccion': cliente.direccion,
        'fecha_nacimiento': fecha_nacimiento_formateada,  # Formato de fecha cambiado
        'solicitudes': solicitudes,
        'grupo_cliente': grupo_cliente,
        'grupo_tecnico': grupo_tecnico,
        'grupo_abogado_causas': grupo_abogado_causas,
        'grupo_abogado_admin': grupo_abogado_admin
    }
    return render(request, 'abogados/VistaCliente.html', context)

@login_required
@user_passes_test(is_abogado_admin)
def register_abogado(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, 'abogados/VistaAbogadoAdministrador')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Un usuario con ese correo ya existe")
            return render(request, 'abogados/VistaAbogadoAdministrador.html')

        try:
            with transaction.atomic():
                user = User.objects.create(
                    username=email,
                    email=email,
                    password=make_password(password),
                    first_name=first_name,
                    last_name=last_name
                )
                Abogado.objects.create(
                    user=user,
                    rut_abogado=rut,
                    nombre=first_name,
                    apellido=last_name,
                    correo_electronico=email,
                    direccion=address,
                    telefono=phone,
                    fecha_nacimiento=date_of_birth
                )
                # Asignar al grupo
                group = Group.objects.get(name='Abogado_Causas')
                user.groups.add(group)
                messages.success(request, "Abogado registrado exitosamente")
                return redirect('VistaAbogadoAdministrador')
        except Exception as e:
            messages.error(request, f"Error al registrar el abogado: {str(e)}")
            return render(request, 'abogados/VistaAbogadoAdministrador')

    return render(request, 'abogados/VistaAbogadoAdministrador.html')

def register_cliente(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden")
            return render(request, 'abogados/registro_cliente.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Un usuario con ese correo ya existe")
            return render(request, 'abogados/registro_cliente.html')#Se cambio la ruta, la que estaba era abogados/registro_cliente.html

        try:
            with transaction.atomic():
                user = User.objects.create(
                    username=email,
                    email=email,
                    password=make_password(password),
                    first_name=first_name,
                    last_name=last_name
                )
                Cliente.objects.create(
                    user=user,
                    rut_cliente=rut,
                    nombre=first_name,
                    apellido=last_name,
                    correo_electronico=email,
                    direccion=address,
                    telefono=phone,
                    fecha_nacimiento=date_of_birth
                )
                # Asignar al grupo
                group = Group.objects.get(name='Cliente')
                user.groups.add(group)
                messages.success(request, "Cliente registrado exitosamente")
                return redirect('Inicio')
        except Exception as e:
            messages.error(request, f"Error al registrar el cliente: {str(e)}")
            return render(request, 'abogados/Registro.html')

    return render(request, 'abogados/VistaCliente.html')




@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        cliente = user.cliente
        cliente.nombre = request.POST.get('nombre', cliente.nombre)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.direccion = request.POST.get('direccion', cliente.direccion)
        try:
            cliente.save()
            messages.success(request, "Perfil actualizado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el perfil: {e}")
        return redirect('VistaCliente')  # O redirige a donde consideres apropiado
    else:
        return render(request, 'abogados/VistaCliente.html', {'user': request.user})



def vista_cliente(request):
    solicitudes = SolicitudServicio.objects.filter(usuario=request.user)
    
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('VistaCliente')  # Asegúrate de que esta URL esté correctamente definida en tus urls.py
    else:
        form = SolicitudServicioForm()
        
    return render(request, 'abogados/VistaCliente.html', {'solicitudes': solicitudes, 'form': form})

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('vista_cliente')
    else:
        form = SolicitudServicioForm()
    return render(request, 'abogados/crearsolicitud.html', {'form': form})

def actualizar_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudServicio, pk=pk)
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, request.FILES, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('vista_cliente')
    else:
        form = SolicitudServicioForm(instance=solicitud)
    return render(request, 'abogados/actualizar_solicitud.html', {'form': form})

def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudServicio, pk=pk)
    solicitud.delete()
    return redirect('vista_cliente')


from django.shortcuts import render, redirect
from .models import SolicitudServicio
from .forms import SolicitudServicioForm

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_solicitudes')  # Redirige a la lista de solicitudes después de guardar
    else:
        form = SolicitudServicioForm()
    
    return render(request, 'abogados/crear_solicitud.html', {'form': form})

def lista_solicitudes(request):
    solicitudes = SolicitudServicio.objects.all()
    return render(request, 'abogados/lista_solicitudes.html', {'solicitudes': solicitudes})



@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user  # Asignar el cliente (usuario autenticado)
            solicitud.save()
            return redirect('crear_solicitud')  # Redirigir a la misma vista para limpiar el formulario
    else:
        form = SolicitudServicioForm()

    solicitudes = SolicitudServicio.objects.filter(cliente=request.user)

    return render(request, 'abogados/VistaCliente.html', {'form': form, 'solicitudes': solicitudes})


def custom_logout(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('Inicio')
    return redirect('Inicio')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Inicio')  # Redirigir a la página de inicio o la que necesites
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
            return render(request, 'abogados/Inicio.html')  # Asegúrate de que esta plantilla es la correcta

    return render(request, 'abogados/Inicio.html')  # Asegúrate de que esta plantilla es la correcta
