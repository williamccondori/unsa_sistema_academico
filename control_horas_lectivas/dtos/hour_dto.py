from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto

class HourDto(object):

    def __init__(self, id=0, quantity=0, id_hour_type=0
        , hour_type_dto=HourTypeDto(), estado=0):
        self.Id = id
        self.Quantity = quantity
        self.IdHourType = id_hour_type
        self.Estado = estado

        self.HourTypeDto = hour_type_dto

    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Quantity = json_data["Quantity"]
        self.IdHourType = json_data["IdHourType"]
        self.Estado = json_data["Estado"]
