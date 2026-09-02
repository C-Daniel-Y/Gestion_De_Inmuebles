"""URL configuration for Gestión de Inmuebles."""

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from inmuebles_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('404/', views.not_found, name='not_found'),
]

# Static assets are exposed explicitly for the local evaluation server.
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR}),
]
handler404 = 'inmuebles_app.views.not_found'
