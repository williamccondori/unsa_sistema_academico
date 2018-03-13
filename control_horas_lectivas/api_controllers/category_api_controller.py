from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from control_horas_lectivas.dtos.response import Response
from control_horas_lectivas.dtos.category_dto import CategoryDto
from control_horas_lectivas.servicios.category_service import CategoryService
import control_horas_lectivas.utilidades.parseador_json as encode


class CategoryApiController(View):

    def get(self, request, *args, **kwargs):
        try:
            category_service = CategoryService()

            result = category_service.get()
            
            return JsonResponse(encode.to_json(
                Response(datos=result)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def post(self, request, *args, **kwargs):
        try:
            category_service = CategoryService()
            category_dto = CategoryDto()

            json_data = encode.to_json_object(request.body)
            category_dto.from_json(json_data)
            category_service.save(category_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)

    def delete(self, request, *args, **kwargs):
        try:
            category_service = CategoryService()
            category_dto = CategoryDto()

            category_dto.from_json(request.GET)
            category_service.delete(category_dto)

            return JsonResponse(encode.to_json(
                Response(datos=True)), safe=False)
        except Exception as e:
            return JsonResponse(encode.to_json(
                Response(estado=False, mensaje=str(e))), safe=False)
