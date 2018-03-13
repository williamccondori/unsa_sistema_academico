from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.semester_type_dto import SemesterTypeDto
from control_horas_lectivas.servicios.semester_type_service import SemesterTypeService
import control_horas_lectivas.utilidades.parseador_json as encode


class SemesterTypeApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            semester_type_service = SemesterTypeService()

            result = semester_type_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            semester_type_service = SemesterTypeService()
            semester_type_dto = SemesterTypeDto()

            json_data = encode.to_json_object(request.body)
            semester_type_dto.from_json(json_data)
            semester_type_service.save(semester_type_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            semester_type_service = SemesterTypeService()
            semester_type_dto = SemesterTypeDto()

            semester_type_dto.from_json(request.GET)
            semester_type_service.delete(semester_type_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
