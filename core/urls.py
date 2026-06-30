from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_convenios, name="lista_convenios"),
    path("nuevo/", views.crear_convenio, name="crear_convenio"),
]