"""URL configuration for Gestión de Inmuebles."""

from django.contrib import admin
from django.urls import path, include

from inmuebles_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('404/', views.not_found, name='not_found'),
    path('inmuebles_app/', include('inmuebles_app.urls')),
]

handler404 = 'inmuebles_app.views.not_found'
