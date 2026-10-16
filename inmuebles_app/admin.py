from django.contrib import admin
from .models import (
    Pais, Region, Provincia, Comuna, Direccion,
    Inmobiliaria, TipoInmueble, TipoOperacion, EstadoInmueble, Caracteristica,
    Propietario, Agente, Cliente, Inmueble, InmuebleCaracteristica,
    Visita, HistorialEstadoInmueble, OperacionContrato
)


admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Inmobiliaria)
admin.site.register(TipoInmueble)
admin.site.register(TipoOperacion)
admin.site.register(EstadoInmueble)
admin.site.register(Caracteristica)
admin.site.register(Propietario)
admin.site.register(Agente)
admin.site.register(Cliente)
admin.site.register(Inmueble)
admin.site.register(InmuebleCaracteristica)
admin.site.register(Visita)
admin.site.register(HistorialEstadoInmueble)
admin.site.register(OperacionContrato)
