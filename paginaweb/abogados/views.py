from django.shortcuts import render

def inicio(request):
    context={}
    return render(request,'abogados/inicio.html', context)

def Formulario(request):
    context={}
    return render(request,'abogados/Formulario.html', context)

def Sobre_nosotros(request):
    context={}
    return render(request,'abogados/Sobre_nosotros.html', context)

