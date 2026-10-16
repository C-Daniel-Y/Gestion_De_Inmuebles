from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Pais, Region, Provincia, Comuna, Direccion,
    Inmobiliaria, TipoInmueble, TipoOperacion, EstadoInmueble, Caracteristica,
    Propietario, Agente, Cliente, Inmueble, InmuebleCaracteristica,
    Visita, HistorialEstadoInmueble, OperacionContrato
)
from .serializer import (
    PaisSerializer, RegionSerializer, ProvinciaSerializer, ComunaSerializer, DireccionSerializer,
    InmobiliariaSerializer, TipoInmuebleSerializer, TipoOperacionSerializer, EstadoInmuebleSerializer,
    CaracteristicaSerializer, PropietarioSerializer, AgenteSerializer, ClienteSerializer,
    InmuebleSerializer, InmuebleCaracteristicaSerializer, VisitaSerializer,
    HistorialEstadoInmuebleSerializer, OperacionContratoSerializer
)


def home(request):
    """Render the public welcome page."""
    return render(request, 'index.html')


def not_found(request, exception=None):
    """Render the branded 404 page for missing routes."""
    return render(request, '404.html', status=404)


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class InmobiliariaViewSet(viewsets.ModelViewSet):
    queryset = Inmobiliaria.objects.all()
    serializer_class = InmobiliariaSerializer


class TipoInmuebleViewSet(viewsets.ModelViewSet):
    queryset = TipoInmueble.objects.all()
    serializer_class = TipoInmuebleSerializer


class TipoOperacionViewSet(viewsets.ModelViewSet):
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer


class EstadoInmuebleViewSet(viewsets.ModelViewSet):
    queryset = EstadoInmueble.objects.all()
    serializer_class = EstadoInmuebleSerializer


class CaracteristicaViewSet(viewsets.ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer


class InmuebleCaracteristicaViewSet(viewsets.ModelViewSet):
    queryset = InmuebleCaracteristica.objects.all()
    serializer_class = InmuebleCaracteristicaSerializer


class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer


class HistorialEstadoInmuebleViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoInmueble.objects.all()
    serializer_class = HistorialEstadoInmuebleSerializer


class OperacionContratoViewSet(viewsets.ModelViewSet):
    queryset = OperacionContrato.objects.all()
    serializer_class = OperacionContratoSerializer
