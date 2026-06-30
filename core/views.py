
# Create your views here.
from django.shortcuts import render, redirect
from .models import Convenio, Provincia
from .forms import ConvenioForm


def lista_convenios(request):

    provincias = Provincia.objects.all()

    convenios = Convenio.objects.all()

    provincia_id = request.GET.get("provincia")

    if provincia_id:
        convenios = convenios.filter(provincia_id=provincia_id)

    return render(
        request,
        "convenios.html",
        {
            "convenios": convenios,
            "provincias": provincias,
            "provincia_seleccionada": provincia_id,
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