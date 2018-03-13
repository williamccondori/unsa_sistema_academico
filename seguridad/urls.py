from django.urls import path, include
from . import views
from seguridad.controllers.login_controller import LoginController

urlpatterns = [
    path('', LoginController.as_view(), name='login'),
]