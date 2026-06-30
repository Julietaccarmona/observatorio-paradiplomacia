
# Create your views here.
from django.shortcuts import render, redirect
from .models import Convenio, Provincia
from .forms import ConvenioForm


def lista_convenios(request):

    convenios = Convenio.objects.all()

    provincias = Provincia.objects.all()

    return render(
        request,
        "convenios.html",
        {
            "convenios": convenios,
            "provincias": provincias,
        },
    )


def crear_convenio(request):
    if request.method == 'POST':
        form = ConvenioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ConvenioForm()
    return render(request, 'crear_convenio.html', {'form': form})