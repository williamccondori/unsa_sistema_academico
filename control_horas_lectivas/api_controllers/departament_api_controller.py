from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.departament_dto import DepartamentDto
from control_horas_lectivas.servicios.departament_service import DepartamentService
import control_horas_lectivas.utilidades.parseador_json as encode


class DepartamentApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            departament_service = DepartamentService()
            
            result = departament_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            departament_service = DepartamentService()
            departament_dto = DepartamentDto()

            json_data = encode.to_json_object(request.body)
            departament_dto.from_json(json_data)
            departament_service.save(departament_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            departament_service = DepartamentService()
            departament_dto = DepartamentDto()

            departament_dto.from_json(request.GET)
            departament_service.delete(departament_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
