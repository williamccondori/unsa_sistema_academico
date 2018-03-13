from control_horas_lectivas.models import Teacher, Day
from control_horas_lectivas.dtos.carga_efectiva_dto import CargaEfectivaDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
from control_horas_lectivas.dtos.departament_dto import DepartamentDto
from control_horas_lectivas.dtos.category_dto import CategoryDto
from control_horas_lectivas.dtos.regime_dto import RegimeDto

class CargaEfectivaService(object):

    def get(self, teacher_id):
        carga_efectiva_dto = CargaEfectivaDto()

        teacher = Teacher.objects.filter(pk=teacher_id)
        teacher = teacher[0]
        carga_efectiva_dto.TeacherDto = TeacherDto(
            teacher.id
            , teacher.name
            , teacher.address_name
            , teacher.degree
            , teacher.speciality
            , teacher.departament_id
            , teacher.category_id
            , teacher.regime_id
            , DepartamentDto(
                teacher.departament.id
                , teacher.departament.name
            )
            , CategoryDto(
                teacher.category.id
                , teacher.category.name
            )
            , RegimeDto(
                teacher.regime.id
                , teacher.regime.name
            )
        )
        
        carga_efectiva_dto.DaysDto = []
        return carga_efectiva_dto

    def save(self, category_dto):
        pass

    def delete(self, category_dto):
        pass