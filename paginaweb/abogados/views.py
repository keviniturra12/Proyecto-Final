from django.shortcuts import render

def Inicio(request):
    context={}
    return render(request,'abogados/Inicio.html', context)

def Registro(request):
    context={}
    return render(request,'abogados/Registro.html', context)

def Sobre_nosotros(request):
    context={}
    return render(request,'abogados/Sobre_nosotros.html', context)

def TecnicoJuridico(request):
    context={}
    return render(request,'abogados/TecnicoJuridico.html', context)

def VistaAbogadoAdministrador(request):
    context={}
    return render(request,'abogados/VistaAbogadoAdministrador.html', context)

def VistaAbogadoConsultor(request):
    context={}
    return render(request,'abogados/VistaAbogadoConsultor.html', context)

def VistaCliente(request):
    context={}
    return render(request,'abogados/VistaCliente.html', context)

