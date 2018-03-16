from control_horas_lectivas.models import Teacher
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
from control_horas_lectivas.dtos.departament_dto import DepartamentDto
from control_horas_lectivas.dtos.category_dto import CategoryDto
from control_horas_lectivas.dtos.regime_dto import RegimeDto

class TeacherService(object):

    def get(self):
        teachers_dto = []
        teachers = Teacher.objects.all()
        for teacher in teachers:
            teachers_dto.append(TeacherDto(
                teacher.id
                , teacher.name
                , teacher.address_name
                , teacher.degree
                , teacher.speciality
                , teacher.departament_id
                , teacher.category.id
                , teacher.regime_id
                , DepartamentDto(
                    teacher.departament.id
                    , teacher.departament.name
                ), CategoryDto(
                    teacher.category.id
                    , teacher.category.name
                ), RegimeDto(
                    teacher.regime.id
                    , teacher.regime.name
                )
            ))
        return teachers_dto
        
    def save(self, teacher_dto):
        if (teacher_dto.Estado == 1):
            teacher = Teacher(
                name=teacher_dto.Name
                , address_name=teacher_dto.AddressName
                , degree=teacher_dto.Degree
                , speciality=teacher_dto.Speciality
                , departament_id=teacher_dto.IdDepartament
                , category_id=teacher_dto.IdCategory
                , regime_id=teacher_dto.IdRegime
            )
            teacher.save()
        elif (teacher_dto.Estado == 2):
            teacher = Teacher.objects.filter(pk=teacher_dto.Id)
            teacher.update(
                name=teacher_dto.Name
                , address_name=teacher_dto.AddressName
                , degree=teacher_dto.Degree
                , speciality=teacher_dto.Speciality
                , departament_id=teacher_dto.IdDepartament
                , category_id=teacher_dto.IdCategory
                , regime_id=teacher_dto.IdRegime
            )
        else:
            return

    def delete(self, teacher_dto):
        teacher = Teacher.objects.filter(pk=teacher_dto.Id)
        teacher.delete()
    