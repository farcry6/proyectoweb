
from .models import Pagina
from django.shortcuts import render, get_object_or_404

from django.template import RequestContext
# Create your views here.

def paginas_list(request):
    paginas = Pagina.objects.filter(estado="publicado")
    return render(request,
                  'home.html',{'paginas': paginas})

                  

