from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.servicios.hour_service import HourService
import control_horas_lectivas.utilidades.parseador_json as encode


class HourApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            hour_service = HourService()

            result = hour_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            hour_service = HourService()
            hour_dto = HourDto()

            json_data = encode.to_json_object(request.body)
            hour_dto.from_json(json_data)
            hour_service.save(hour_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            hour_service = HourService()
            hour_dto = HourDto()

            hour_dto.from_json(request.GET)
            hour_service.delete(hour_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
