from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.course_dto import CourseDto
from control_horas_lectivas.servicios.course_service import CourseService
import control_horas_lectivas.utilidades.parseador_json as encode


class CourseApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            if 'IdStudyPlan' in request.GET:
                id_study_plan = int(request.GET['IdStudyPlan'])
                result = self.get_course_by_study_plan(id_study_plan)
            else:
                result = self.get_course()

            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def get_course(self):
        # course_service = CourseService()
        # return course_service.get() 
        pass

    def get_course_by_study_plan(self, id_study_plan):
        course_service = CourseService()
        return course_service.get_by_study_plan(id_study_plan) 

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
