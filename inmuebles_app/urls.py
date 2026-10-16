from django.urls import path, include
from rest_framework import routers
from inmuebles_app import views

enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)
enrutador.register(r'direcciones', views.DireccionViewSet)
enrutador.register(r'inmobiliarias', views.InmobiliariaViewSet)
enrutador.register(r'tipos-inmueble', views.TipoInmuebleViewSet)
enrutador.register(r'tipos-operacion', views.TipoOperacionViewSet)
enrutador.register(r'estados-inmueble', views.EstadoInmuebleViewSet)
enrutador.register(r'caracteristicas', views.CaracteristicaViewSet)
enrutador.register(r'propietarios', views.PropietarioViewSet)
enrutador.register(r'agentes', views.AgenteViewSet)
enrutador.register(r'clientes', views.ClienteViewSet)
enrutador.register(r'inmuebles', views.InmuebleViewSet)
enrutador.register(r'inmuebles-caracteristicas', views.InmuebleCaracteristicaViewSet)
enrutador.register(r'visitas', views.VisitaViewSet)
enrutador.register(r'historial-estados', views.HistorialEstadoInmuebleViewSet)
enrutador.register(r'operaciones', views.OperacionContratoViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]
