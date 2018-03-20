from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.informacion_dto import InformacionDto
from control_horas_lectivas.servicios.informacion_service import InformacionService
import control_horas_lectivas.utilidades.parseador_json as encode

class InformacionApiController(View):
    def get(self, request, *args, **kwargs):
        try:
            informacion_service = InformacionService()
            username = request.session.get('username', False)
            if username is False:
                raise ValueError('No se encuentra la sesión del usuario')   
            id_departamento = request.session.get('id_departamento', False)
            if id_departamento is False:
                raise ValueError('No se ha registrado el código del departamento del usuario')
            id_plan_estudio = request.session.get('id_plan_estudio', False)
            print(id_plan_estudio)
            resultado = informacion_service.obtener(username, id_departamento, id_plan_estudio)
            return JsonResponse(encode.to_json(
                Response(datos=resultado)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
