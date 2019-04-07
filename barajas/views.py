from django.shortcuts import render
from django.http import HttpResponse
from barajas.models import card

# Create your views here.

def formularioIngreso(request):
    return render(request, 'FormIngreso.html')

def buscar(request):
    if 'q' in request.GET and request.GET['q']:
        mensaje="Estas buscando: %r"% request.GET['q']
    else:
        mensaje="Has subido un formulario vacio."
    return HttpResponse(mensaje)

#def ingreso(request):
    #error=False
    #numero=request.GET['numero']
    #nombre=request.GET['nombre']
    #habilidad=request.GET['habilidad']
    #p1=card.objects.create(id=numero,Nombre=nombre,Habilidad=habilidad)
    #return render(request, 'FormIngreso.html',{'ingreso':True})

def ingreso(request):
    error=False
    if 'numero' in request.GET:#si se ha enviado el formulario
        numero=request.GET['numero']
        nombre=request.GET['nombre']
        habilidad=request.GET['habilidad']
        edicion=request.GET['edicion']
        if not numero:#si el formulario esta parcialmente incompleto
            error=True
        else:
            p1=card.objects.create(id=numero,Nombre=nombre,Habilidad=habilidad,Edicion=edicion)
            return render(request, 'FormIngreso.html',{'ingreso':True})
    return render(request,'FormIngreso.html',{'error':error})
    
def selecColeccion(request):
    return render(request,'Buscador.html')
