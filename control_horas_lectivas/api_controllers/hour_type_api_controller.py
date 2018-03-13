from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto
from control_horas_lectivas.servicios.hour_type_service import HourTypeService
import control_horas_lectivas.utilidades.parseador_json as encode


class HourTypeApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            hour_type_service = HourTypeService()

            result = hour_type_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            hour_type_service = HourTypeService()
            hour_type_dto = HourTypeDto()

            json_data = encode.to_json_object(request.body)
            hour_type_dto.from_json(json_data)
            hour_type_service.save(hour_type_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            hour_type_service = HourTypeService()
            hour_type_dto = HourTypeDto()

            hour_type_dto.from_json(request.GET)
            hour_type_service.delete(hour_type_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
