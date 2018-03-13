from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.hour_activity_dto import HourActivityDto
from control_horas_lectivas.servicios.hour_activity_service import HourActivityService
import control_horas_lectivas.utilidades.parseador_json as encode


class HourActivityApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            hour_activity_service = HourActivityService()

            result = hour_activity_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            hour_activity_service = HourActivityService()
            hour_activity_dto = HourActivityDto()

            json_data = encode.to_json_object(request.body)
            hour_activity_dto.from_json(json_data)
            hour_activity_service.save(hour_activity_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            hour_activity_service = HourActivityService()
            hour_activity_dto = HourActivityDto()

            hour_activity_dto.from_json(request.GET)
            hour_activity_service.delete(hour_activity_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
