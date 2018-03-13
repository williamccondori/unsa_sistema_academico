from control_horas_lectivas.models import Hour, HourType
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto

class HourService(object):

    def get(self):
        hours_dto = []
        hours = Hour.objects.all()
        for hour in hours:
            hours_dto.append(HourDto(
                hour.id
                , hour.quantity
                , hour.hour_type_id
                , HourTypeDto(
                    hour.hour_type.id
                    , hour.hour_type.name
                )
            ))
        return hours_dto

    def save(self, hour_dto):
        if (hour_dto.Estado == 1):
            hour = Hour(
                hour_type_id=hour_dto.IdHourType
                , quantity=hour_dto.Quantity
            )
            hour.save()
        elif (hour_dto.Estado == 2):
            hour = Hour.objects.filter(pk=hour_dto.Id)
            hour.update(
                hour_type_id=hour_dto.IdHourType
                , quantity=hour_dto.Quantity
            )
        else:
            return

    def delete(self, hour_dto):
        hour = Hour.objects.filter(pk=hour_dto.Id)
        hour.delete()
