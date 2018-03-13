from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
from control_horas_lectivas.servicios.teacher_service import TeacherService
import control_horas_lectivas.utilidades.parseador_json as encode


class TeacherApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            teacher_service = TeacherService()

            result = teacher_service.get()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            teacher_service = TeacherService()
            teacher_dto = TeacherDto()

            json_data = encode.to_json_object(request.body)
            teacher_dto.from_json(json_data)
            teacher_service.save(teacher_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            teacher_service = TeacherService()
            teacher_dto = TeacherDto()

            teacher_dto.from_json(request.GET)
            teacher_service.delete(teacher_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
