from control_horas_lectivas.models import HourActivity, HourType
from control_horas_lectivas.dtos.hour_activity_dto import HourActivityDto
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto

class HourActivityService(object):

    def get(self):
        hour_activities_dto = []
        hour_activities = HourActivity.objects.all()
        for hour_Activity in hour_activities:
            hour_activities_dto.append(HourActivityDto(
                hour_Activity.id
                , hour_Activity.quantity
                , hour_Activity.hour_type_id
                , HourTypeDto(
                    hour_Activity.hour_type.id
                    , hour_Activity.hour_type.name
                )
            ))
        return hour_activities_dto

    def save(self, hour_activity_dto):
        if (hour_activity_dto.Estado == 1):
            hour_activity = HourActivity(
                hour_type_id=hour_activity_dto.IdHourType
                , quantity=hour_activity_dto.Quantity
            )
            hour_activity.save()
        elif (hour_activity_dto.Estado == 2):
            hour = HourActivity.objects.filter(pk=hour_activity_dto.Id)
            hour.update(
                hour_type_id=hour_activity_dto.IdHourType
                , quantity=hour_activity_dto.Quantity
            )
        else:
            return

    def delete(self, hour_activity_dto):
        hour = HourActivity.objects.filter(pk=hour_activity_dto.Id)
        hour.delete()
