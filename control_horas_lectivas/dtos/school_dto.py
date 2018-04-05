from control_horas_lectivas.dtos.departament_dto import DepartamentDto

class SchoolDto(object):

    def __init__(self, id=0, name='', id_departament=0
        , departament_dto=DepartamentDto(), estado=0):
        self.Id = id
        self.Name = name
        self.IdDepartament = id_departament
        self.Estado = estado
        self.DepartamentDto = departament_dto

    def from_json(self, json_data):
        self.IdDepartament = 0
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.Estado = json_data["Estado"]