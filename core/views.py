
# Create your views here.
from django.shortcuts import render, redirect
from .models import Convenio, Provincia
from .forms import ConvenioForm

def lista_convenios(request):

    provincias = Provincia.objects.all()

    paises = (
        Convenio.objects
        .values_list("pais", flat=True)
        .distinct()
        .order_by("pais")
    )

    convenios = Convenio.objects.all()

    provincia_id = request.GET.get("provincia")
    pais = request.GET.get("pais")
    tema = request.GET.get("tema")
    estado = request.GET.get("estado")
    tipo = request.GET.get("tipo")

    if provincia_id:
        convenios = convenios.filter(provincia_id=provincia_id)

    if pais:
        convenios = convenios.filter(pais=pais)

    if tema:
        convenios = convenios.filter(tema=tema)

    if estado:
        convenios = convenios.filter(estado=estado)

    if tipo:
        convenios = convenios.filter(tipo_acuerdo=tipo)

    return render(
        request,
        "convenios.html",
        {
            "convenios": convenios,
            "provincias": provincias,
            "paises": paises,

            "provincia_seleccionada": provincia_id,
            "pais_seleccionado": pais,
            "tema_seleccionado": tema,
            "estado_seleccionado": estado,
            "tipo_seleccionado": tipo,

            "temas": Convenio.TEMAS,
            "estados": Convenio.ESTADOS,
            "tipos": Convenio.TIPOS_ACUERDO,
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