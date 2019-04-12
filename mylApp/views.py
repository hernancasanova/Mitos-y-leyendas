from django.http import HttpResponse
from django.shortcuts import render

def hola(request):
    return HttpResponse("Function hola")

def atributos_meta(request):
    valor=request.META.items()
    valor.sort()
    html=[]
    for k,v in valor:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))

def seccion(request):
    return render(request,"inicio.html",{'seccion':'inicio'})
    #return HttpResponse("")

def primera_era(request):
    return render(request,"primera_era.html",{'seccion':'inicio'})
    #return HttpResponse("")

def faltantesReto(request):
    return render(request,"Faltantes_el_reto.html","")

#def formulario_buscar(request):
 #   return render(request, "formulario_buscar.html")

