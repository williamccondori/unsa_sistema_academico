from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.school_dto import SchoolDto
from control_horas_lectivas.servicios.school_service import SchoolService
import control_horas_lectivas.utilidades.parseador_json as encode


class SchoolApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            school_service = SchoolService()
            id_departamento = request.session.get('id_departamento', False)
            if id_departamento is False:
                id_departamento = 0
            result = school_service.obtener_x_departamento(id_departamento)
            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            school_service = SchoolService()
            school_dto = SchoolDto()
            id_departamento = request.session.get('id_departamento', False)
            if id_departamento is False:
                id_departamento = 0
            json_data = encode.to_json_object(request.body)
            school_dto.from_json(json_data)
            school_dto.IdDepartament = id_departamento
            school_service.save(school_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            school_service = SchoolService()
            school_dto = SchoolDto()

            school_dto.from_json(request.GET)
            school_service.delete(school_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
