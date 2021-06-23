from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Orla,Curso

def orla_list(request):
    orlas = Orla.objects.filter(estado='estado')
    return render(request, 'index.html',
                {'orlas': orlas})