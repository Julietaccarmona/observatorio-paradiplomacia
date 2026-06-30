from django import forms
from .models import Convenio


class ConvenioForm(forms.ModelForm):

    class Meta:
        model = Convenio

        fields = [
            "provincia",
            "actores",
            "pais",
            "tipo_acuerdo",
            "tema",
            "fecha_firma",
            "estado",
            "descripcion",
            "enlace_documento",
        ]