from django.urls import path, include
from . import views
from control_horas_lectivas.controllers.departamento_controller import DepartamentoController
from control_horas_lectivas.controllers.login_controller import LoginController

urlpatterns = [
    path('api/', include('control_horas_lectivas.urls_api')),
    path('', views.dashboard, name='dashboard'),
    path('teacher', views.teacher, name='teacher'),
    path('departament', views.departament, name='departament'),
    path('category', views.category, name='category'),
    path('regime', views.regime, name='regime'),
    path('day', views.day, name='day'),
    path('hour_type', views.hourtype, name='hour_type'),
    path('semester', views.semester, name='semester'),
    path('carga_efectiva', views.cargaefectiva, name='carga_efectiva'),
    path('study_plan', views.studyplan, name='study_plan'),
    path('school', views.school, name='school'),
    path('course', views.course, name='course'),
    path('departamento', DepartamentoController.as_view(), name='departamento'),
    path('login', LoginController.as_view(), name='login')
]
