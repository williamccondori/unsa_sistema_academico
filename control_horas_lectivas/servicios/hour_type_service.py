from control_horas_lectivas.models import HourType
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto


class HourTypeService(object):

    def get(self):
        hour_types_dto = []
        hour_types = HourType.objects.all()
        for hour_type in hour_types:
            hour_types_dto.append(HourTypeDto(
                hour_type.id
                , hour_type.name
            ))
        return hour_types_dto

    def save(self, hour_type_dto):
        if (hour_type_dto.Estado == 1):
            hour_type = HourType(
                name=hour_type_dto.Name
            )
            hour_type.save()
        elif (hour_type_dto.Estado == 2):
            hour_type = HourType.objects.filter(pk=hour_type_dto.Id)
            hour_type.update(
                name=hour_type_dto.Name
            )
        else:
            return

    def delete(self, hour_type_dto):
        hour_type = HourType.objects.filter(pk=hour_type_dto.Id)
        hour_type.delete()
