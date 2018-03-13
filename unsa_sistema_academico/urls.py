from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control_horas_lectivas/', include('control_horas_lectivas.urls'))
]
