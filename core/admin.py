from django.contrib import admin
from .models import Provincia, Actor, Convenio


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo")
    search_fields = ("nombre", "tipo")


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = (
        "provincia",
        "pais",
        "tema",
        "estado",
        "fecha_firma",
    )

    list_filter = (
        "provincia",
        "estado",
        "pais",
    )

    search_fields = (
        "pais",
        "tema",
        "descripcion",
    )

    ordering = ("-fecha_firma",)

