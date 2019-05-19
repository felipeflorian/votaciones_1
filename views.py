from django.shortcuts import render,get_object_or_404
from .models import Voto, Votante
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Acá se Crea la visa del archivo your views here.


def index(solicitud):
    return HttpResponse("Hello, world. You're at the polls index.")

def Detalles(solicitud, pregunta_id):
    return HttpResponse("Esta es su opcion %s." % pregunta_id)
def Resultados(solicitud, pregunta_id):
    question = get_object_or_404(Voto, pk=pregunta_id)
    return render(solicitud, 'elecciones/resultados.html', {'question': question})

    #response = "Esta este es el resultado %s."
    #return HttpResponse(response % pregunta_id)

def Voto(solicitud, pregunta_id):
    pregunta = get_obkect_or_404(Voto, pk=pregunta_id)
    try:
        selected_choice = Voto.votesset.get(pk=solicitud.POST['choice'])
    except (KeyError, Voto.DoesNotExist):
        return render(solicitud, 'elecciones/detalles.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('elecciones:resultados', args=(pregunta.id,)))

    return HttpResponse( "tu Voto fue %s." % pregunta_id)
