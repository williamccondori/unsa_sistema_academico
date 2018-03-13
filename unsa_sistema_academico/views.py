from django.shortcuts import HttpResponse

def index(request):
    response = "<a href='/administracion/seguridad'>Ir al administrador</a>"
    return HttpResponse(response)