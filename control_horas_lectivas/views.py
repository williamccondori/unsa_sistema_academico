from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def teacher(request):
    return render(request, 'teacher.html')

def category(request):
    return render(request, 'category.html')

def departament(request):
    return render(request, 'departament.html')

def regime(request):
    return render(request, 'regime.html')

def day(request):
    return render(request, 'day.html')

def semester(request):
    return render(request, 'semester.html')

def cargaefectiva(request):
    return render(request, 'carga_efectiva.html')

def studyplan(request):
    return render(request, 'study_plan.html')

def school(request):
    return render(request, 'school.html')