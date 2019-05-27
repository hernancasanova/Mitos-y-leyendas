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
def inicio(request):
    return render(request,"inicio.html")

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
    if 'selectColeccion' in request.GET:
        coleccion=request.GET['selectColeccion']
        if coleccion == "FaltantesReto" :
            colec=card.objects.all().filter(Edicion=coleccion).order_by("id")
            #colec=card.objects.all()
            print("contenido de colec:  ",colec)
            return render(request,"Faltantes_el_reto.html",{"result":colec})
            #return render(request,"Faltantes_el_reto.html")
        elif coleccion == "FaltantesRetoExtension":
            colec=card.objects.filter(Edicion=coleccion).order_by("id")
            return render(request,"Faltantes_el_reto_extension.html",{"result":colec})
            #return render(request,"Faltantes_el_reto_extension.html")
        else:
            return render(request,"ColeccionIncorrecta.html")
    else:
        return render(request,'Buscador.html')

def edicion(request):
    error=False
    if 'nombre' in request.GET:#si se ha enviado el formulario
        nombre=request.GET['nombre']
        #nombre=request.GET['nombre']
        #habilidad=request.GET['habilidad']
        #edicion=request.GET['edicion']
        #if not numero:#si el formulario esta parcialmente incompleto
        #    error=True
        #else:
            #p1=card.objects.create(id=numero,Nombre=nombre,Habilidad=habilidad,Edicion=edicion)
            #return render(request, 'FormEdit.html',{'ingreso':True})
        carta=card.objects.filter(Nombre=nombre)
        return render(request,'FormEdit.html',{'result':carta})
    else:
            return render(request,"ColeccionIncorrecta.html")

def actualizar(request):
    error=False
    if 'numero' in request.GET:#si se ha enviado el formulario
        numero=request.GET['numero']
        nombre=request.GET['nombre']
        habilidad=request.GET['habilidad']
        edicion=request.GET['edicion']
        if not numero:#si el formulario esta parcialmente incompleto
            error=True
        else:
            c=card(id=numero,Nombre=nombre,Habilidad=habilidad,Edicion=edicion)
            c.save()
            return render(request, 'inicio.html')
    return render(request,'FormIngreso.html',{'error':error})

def eliminar(request):
    error=False
    if 'numero' in request.GET:#si se ha enviado el formulario
        numero=request.GET['numero']
        if not numero:#si el formulario esta parcialmente incompleto
            error=True
        else:
            c=card.objects.get(id=numero)
            c.delete()
            return render(request, 'inicio.html')
    return render(request,'FormIngreso.html',{'error':error})
