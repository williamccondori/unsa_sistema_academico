from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administracion/seguridad/', include('seguridad.urls')),
    path('administracion/control_horas_lectivas/', include('control_horas_lectivas.urls'))
]
