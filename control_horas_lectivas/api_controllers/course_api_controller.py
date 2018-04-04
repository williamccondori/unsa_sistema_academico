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
            id_plan_estudio = request.session.get('id_plan_estudio', False)
            if id_plan_estudio is False:
                id_plan_estudio = 0
            result = course_service.obtener_x_plan_estudio(id_plan_estudio)
            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            course_service = CourseService()
            course_dto = CourseDto()

            id_plan_estudio = request.session.get('id_plan_estudio', False)
            if id_plan_estudio is False:
                id_plan_estudio = 0

            json_data = encode.to_json_object(request.body)
            course_dto.from_json(json_data)
            course_dto.IdPlanEstudio = id_plan_estudio
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
