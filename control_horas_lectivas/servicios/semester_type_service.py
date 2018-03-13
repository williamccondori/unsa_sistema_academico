from control_horas_lectivas.models import SemesterType
from control_horas_lectivas.dtos.semester_type_dto import SemesterTypeDto


class SemesterTypeService(object):

    def get(self):
        semester_types_dto = []
        semester_types = SemesterType.objects.all()
        for semester_type in semester_types:
            semester_types_dto.append(SemesterTypeDto(
                semester_type.id
                , semester_type.name
            ))
        return semester_types_dto

    def save(self, semester_type_dto):
        if (semester_type_dto.Estado == 1):
            semester_type = SemesterType(
                name=semester_type_dto.Name
            )
            semester_type.save()
        elif (semester_type_dto.Estado == 2):
            semester_type = SemesterType.objects.filter(pk=semester_type_dto.Id)
            semester_type.update(
                name=semester_type_dto.Name
            )
        else:
            return

    def delete(self, semester_type_dto):
        semester_type = SemesterType.objects.filter(pk=semester_type_dto.Id)
        semester_type.delete()
