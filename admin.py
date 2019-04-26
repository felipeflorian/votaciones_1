# models here.
from django.contrib import admin
from .models import Partido_politico
from .models import Candidato
from .models import Votante
from .models import Voto

#register models here.
admin.site.register(Partido_politico)
admin.site.register(Candidato)
admin.site.register(Votante)
admin.site.register(Voto)

