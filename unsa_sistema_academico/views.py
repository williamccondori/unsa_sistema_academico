from django.shortcuts import HttpResponse

def index(request):
    response = "<a href='/administracion/control_horas_lectivas/login'>Ir al administrador</a>"
    return HttpResponse(response)