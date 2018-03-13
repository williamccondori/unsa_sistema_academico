from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.regime_dto import RegimeDto
from control_horas_lectivas.servicios.regime_service import RegimeService
import control_horas_lectivas.utilidades.parseador_json as encode


class RegimeApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            regime_service = RegimeService()

            result = regime_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            regime_service = RegimeService()
            regime_dto = RegimeDto()

            json_data = encode.to_json_object(request.body)
            regime_dto.from_json(json_data)
            regime_service.save(regime_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            regime_service = RegimeService()
            regime_dto = RegimeDto()

            regime_dto.from_json(request.GET)
            regime_service.delete(regime_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
