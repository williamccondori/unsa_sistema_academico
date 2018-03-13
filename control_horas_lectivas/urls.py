from django.urls import path, include
from . import views


urlpatterns = [
    path('api/', include('control_horas_lectivas.urls_api')),
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('teacher', views.teacher, name='teacher'),
    path('departament', views.departament, name='departament'),
    path('category', views.category, name='category'),
    path('regime', views.regime, name='regime'),
    path('day', views.day, name='day'),
    path('semester', views.semester, name='semester'),
    path('carga_efectiva', views.cargaefectiva, name='carga_efectiva'),
    path('study_plan', views.studyplan, name='study_plan'),
    path('school', views.school, name='school'),
    
]