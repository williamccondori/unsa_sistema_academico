from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.semester_number_dto import SemesterNumberDto
from control_horas_lectivas.servicios.semester_number_service import SemesterNumberService
import control_horas_lectivas.utilidades.parseador_json as encode


class SemesterNumberApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            semester_number_service = SemesterNumberService()

            result = semester_number_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            semester_number_service = SemesterNumberService()
            semester_number_dto = SemesterNumberDto()

            json_data = encode.to_json_object(request.body)
            semester_number_dto.from_json(json_data)
            semester_number_service.save(semester_number_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            semester_number_service = SemesterNumberService()
            semester_number_dto = SemesterNumberDto()

            semester_number_dto.from_json(request.GET)
            semester_number_service.delete(semester_number_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
