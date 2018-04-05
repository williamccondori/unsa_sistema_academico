from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.carga_efectiva_dto import CargaEfectivaDto
from control_horas_lectivas.servicios.carga_efectiva_service import CargaEfectivaService
import control_horas_lectivas.utilidades.parseador_json as encode


class CargaEfectivaApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            carga_efectiva_service = CargaEfectivaService()
            username = request.session.get('username', False)
            if username is False:
                username = None
            result = carga_efectiva_service.get(username)
            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)