from django.shortcuts import render
from teatrodidatico.models import *
from .helpers import load_curriculo, load_premios
from datetime import datetime

# Create your views here.
def index(request):
    espetaculos = Espetaculo.objects.filter(ativo=True)
    fotos_espetaculos = Fotos.objects.filter(ativo=True)
    integrantes = Integrantes.objects.filter(ativo=True)    
    curriculos = Curriculo.objects.order_by('-data').filter(ativo=True)
    premios = load_premios(curriculos.filter(tipo='2'))
    curriculo = load_curriculo(curriculos.filter(tipo='1'))
    cursos = Cursos.objects.filter(ativo=True)
    agenda = Agenda.objects.order_by('-data').filter(ativo=True)
    agenda_passada = agenda.filter(data_final__lte=datetime.now()) #lte = less than or equal to
    agenda_futura = agenda.filter(data_final__gte=datetime.now()) #lte = greater than or equal to

#    @property
#    def data_passou(self):
#        return date.today() > self.date

    dados = {
        'espetaculos': espetaculos,
        'fotos_espetaculos' : fotos_espetaculos,
        'integrantes': integrantes,
        'agenda_passada' : agenda_passada,
        'agenda_futura' : agenda_futura,
        'cursos' : cursos,
        'load_premios' : premios,        
        'load_curriculo' : curriculo,
    }
    
    return render(request, "index.html", dados)

def cursos(request, curso_id):
    cursos = Cursos.objects.filter(ativo=True, id=curso_id)
    programa = ProgramaCurso.objects.filter(ativo=True)
    textos = Textos.objects.filter(ativo=True)
    
    dados = {
        'cursos' : cursos,
        'programa' : programa,
        'textos' : textos
    }

    return render(request, "cursos.html", dados)