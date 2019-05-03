from django.shortcuts import render

# Acá se Crea la visa del archivo your views here.

def index(solicitud):
    return HttpResponse("Hello, world. You're at the polls index.")

def Detalles(solicitud, pregunta_id):
    return HttpResponse("Esta es su opcion %s." % pregunta_id)
def Resultados(solicitud, pregunta_id):
    response = "Esta este es el resultado %s."
    return HttpResponse(response % pregunta_id)

def Voto( solicitud, pregunta_id):
    return HttpResponse( "tu Voto fue %s." % pregunta_id)
