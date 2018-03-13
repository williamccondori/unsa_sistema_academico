from control_horas_lectivas.models import Day
from control_horas_lectivas.dtos.day_dto import DayDto


class DayService(object):

    def get(self):
        days_dto = []
        days = Day.objects.all().order_by('order')
        for day in days:
            days_dto.append(DayDto(
                day.id
                , day.name
                , day.order
                , day.name[0].upper()
            ))
        return days_dto

    def save(self, day_dto):
        if (day_dto.Estado == 1):
            day = Day(
                name=day_dto.Name
                , order=day_dto.Order
            )
            day.save()
        elif (day_dto.Estado == 2):
            day = Day.objects.filter(pk=day_dto.Id)
            day.update(
                name=day_dto.Name
                , order=day_dto.Order
            )
        else:
            return

    def delete(self, day_dto):
        day = Day.objects.filter(pk=day_dto.Id)
        day.delete()
