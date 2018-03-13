from control_horas_lectivas.models import School
from control_horas_lectivas.dtos.school_dto import SchoolDto
from control_horas_lectivas.dtos.departament_dto import DepartamentDto


class SchoolService(object):

    def get(self):
        schools_dto = []
        schools = School.objects.all()

        for school in schools:
            schools_dto.append(SchoolDto(
                school.id
                , school.name
                , school.departament_id
                , DepartamentDto(
                    school.departament.id
                    , school.departament.name
                )
            ))
        return schools_dto

    def save(self, school_dto):
        if (school_dto.Estado == 1):
            school = School(
                name=school_dto.Name
                , departament_id=school_dto.IdDepartament
            )
            school.save()
        elif (school_dto.Estado == 2):
            school = School.objects.filter(pk=school_dto.Id)
            school.update(
                name=school_dto.Name
                , departament_id=school_dto.IdDepartament
            )
        else:
            return

    def delete(self, school_dto):
        school = School.objects.filter(pk=school_dto.Id)
        school.delete()
