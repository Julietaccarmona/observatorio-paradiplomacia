from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Convenio

def lista_convenios(request):
    convenios = Convenio.objects.all()
    return render(request, 'convenios.html', {'convenios': convenios})