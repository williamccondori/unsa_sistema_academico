from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.course_dto import CourseDto
from control_horas_lectivas.servicios.course_service import CourseService
import control_horas_lectivas.utilidades.parseador_json as encode


class CourseApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            course_service = CourseService()
            if 'id_plan_estudio' in request.GET:
                id_plan_estudio = int(request.GET['id_plan_estudio'])
                result = course_service.obtener_x_plan_estudio(id_plan_estudio)
            else:
                result = []
            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            course_service = CourseService()
            course_dto = CourseDto()

            json_data = encode.to_json_object(request.body)
            course_dto.from_json(json_data)
            course_service.save(course_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:

            course_service = CourseService()
            course_dto = CourseDto()

            course_dto.from_json_delete(request.GET)
            course_service.delete(course_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
