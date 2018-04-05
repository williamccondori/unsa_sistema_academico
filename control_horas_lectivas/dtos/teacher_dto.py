from control_horas_lectivas.dtos.departament_dto import DepartamentDto
from control_horas_lectivas.dtos.category_dto import CategoryDto
from control_horas_lectivas.dtos.regime_dto import RegimeDto

class TeacherDto(object):

    def __init__(self, id=0, name='', address_name='', degree=''
        , speciality='', id_departament=0, id_category=0, id_regime=0
        , departament_dto=DepartamentDto(), category_dto=CategoryDto()
        , regime_dto=RegimeDto(), courses_dto=[], estado=0):
        self.Id = id
        self.Name = name
        self.AddressName = address_name
        self.Degree = degree
        self.Speciality = speciality
        self.IdDepartament = id_departament
        self.IdCategory = id_category
        self.IdRegime = id_regime
        self.DepartamentDto = departament_dto
        self.CategoryDto = category_dto
        self.Regime = regime_dto
        self.CoursesDto = courses_dto

        self.Estado = estado

    def from_json(self, json_data):
        self.IdDepartament = 0
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.AddressName = json_data["AddressName"]
        self.Degree = json_data["Degree"]
        self.Speciality = json_data["Speciality"]
        self.IdCategory = json_data["IdCategory"]
        self.IdRegime = json_data["IdRegime"]
        self.Estado = json_data["Estado"]