from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('administracion/control_horas_lectivas/', include('control_horas_lectivas.urls'))
]
