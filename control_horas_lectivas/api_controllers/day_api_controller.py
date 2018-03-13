from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.day_dto import DayDto
from control_horas_lectivas.servicios.day_service import DayService
import control_horas_lectivas.utilidades.parseador_json as encode


class DayApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            day_service = DayService()

            result = day_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            day_service = DayService()
            day_dto = DayDto()

            json_data = encode.to_json_object(request.body)
            day_dto.from_json(json_data)
            day_service.save(day_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            day_service = DayService()
            day_dto = DayDto()

            day_dto.from_json(request.GET)
            day_service.delete(day_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
