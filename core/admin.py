from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Provincia, Actor, Convenio

admin.site.register(Provincia)
admin.site.register(Actor)
admin.site.register(Convenio)