from django.http import HttpResponse
from django.shortcuts import render

def hola(request):
    return HttpResponse("Hola mundo")

def seccion(request):
    return render(request,"inicio.html",{'seccion':'inicio'})
    #return HttpResponse("")

def primera_era(request):
    return render(request,"primera_era.html",{'seccion':'inicio'})
    #return HttpResponse("")
