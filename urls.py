from django.urls import path

from . import views

urlpatterns = [
    # ex: /elecciones/
    path('', views.index, name='index'),
    #ex : /elecciones/5/
    path('<int:pregunta_id>/', views.Detalles, name='Detalles'),
    # ex: /polls/5/Resultados/
    path('<int:pregunta_id>/Resultados/', views.Resultados, name='Resultados'),
    # ex: /polls/5/vote/
    path('<int:pregunta_id>/Voto/', views.Voto, name='Voto'),
]
