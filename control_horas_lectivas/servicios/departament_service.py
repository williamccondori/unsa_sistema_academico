from control_horas_lectivas.models import Departament
from control_horas_lectivas.dtos.departament_dto import DepartamentDto


class DepartamentService(object):

    def get(self):
        departaments_dto = []
        departaments = Departament.objects.all()
        for departament in departaments:
            departaments_dto.append(DepartamentDto(
                departament.id
                , departament.name
            ))
        return departaments_dto

    def save(self, departament_dto):
        if (departament_dto.Estado == 1):
            departament = Departament(
                name=departament_dto.Name
            )
            departament.save()
        elif (departament_dto.Estado == 2):
            departament = Departament.objects.filter(pk=departament_dto.Id)
            departament.update(
                name=departament_dto.Name
            )
        else:
            return

    def delete(self, departament_dto):
        departament = Departament.objects.filter(pk=departament_dto.Id)
        departament.delete()
