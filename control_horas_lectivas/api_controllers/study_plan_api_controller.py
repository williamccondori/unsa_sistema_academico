from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.servicios.study_plan_service import StudyPlanService
import control_horas_lectivas.utilidades.parseador_json as encode


class StudyPlanApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            study_plan_service = StudyPlanService()
            id_departamento = request.session.get('id_departamento', False)
            if id_departamento is False:
                id_departamento = 0
            resultado = study_plan_service.obtener_x_departamento(id_departamento)
            return JsonResponse(encode.to_json(
                Response(datos=resultado)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            study_plan_service = StudyPlanService()
            study_plan_dto = StudyPlanDto()

            json_data = encode.to_json_object(request.body)
            study_plan_dto.from_json(json_data)
            study_plan_service.save(study_plan_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            study_plan_service = StudyPlanService()
            study_plan_dto = StudyPlanDto()

            study_plan_dto.from_json(request.GET)
            study_plan_service.delete(study_plan_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
