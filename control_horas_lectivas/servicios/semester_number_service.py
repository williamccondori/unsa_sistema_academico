from control_horas_lectivas.models import SemesterNumber
from control_horas_lectivas.dtos.semester_number_dto import SemesterNumberDto


class SemesterNumberService(object):

    def get(self):
        semester_numbers_dto = []
        semester_numbers = SemesterNumber.objects.all()
        for semester_number in semester_numbers:
            semester_numbers_dto.append(SemesterNumberDto(
                semester_number.id
                , semester_number.name
            ))
        return semester_numbers_dto

    def save(self, semester_number_dto):
        if (semester_number_dto.Estado == 1):
            semester_number = SemesterNumber(
                name=semester_number_dto.Name
            )
            semester_number.save()
        elif (semester_number_dto.Estado == 2):
            semester_number = SemesterNumber.objects.filter(pk=semester_number_dto.Id)
            semester_number.update(
                name=semester_number_dto.Name
            )
        else:
            return

    def delete(self, semester_number_dto):
        semester_number = SemesterNumber.objects.filter(pk=semester_number_dto.Id)
        semester_number.delete()
