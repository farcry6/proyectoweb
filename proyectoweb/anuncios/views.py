from django.shortcuts import render
from django.http import HttpResponse
from .models import Anuncio
import datetime

# Create your views here.

def home(request):
    return render(request, 'anuncios/home.html')

def hora_actual(request):
    now = datetime.datetime.now()
    html = '<html><body><strong>¡Hola Mundo!</strong><br>Fecha y Hora: %s.</body></html>' % now
    return HttpResponse(html)

def anuncio_list(request):
    anuncios = Anuncio.objects.filter(estado='publicado')
    return render(request, 'anuncios/anuncios.html',
                {'anuncios': anuncios})

def precio(request):
    return render(request,'anuncios/precio.html')


    
def contacto(request):
    return render(request,'anuncios/contacto.html')

def diseño(request):
    return render(request,'anuncios/diseño.html')


 