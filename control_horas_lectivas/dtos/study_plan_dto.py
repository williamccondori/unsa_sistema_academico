from control_horas_lectivas.dtos.school_dto import SchoolDto

class StudyPlanDto(object):

    def __init__(self, id=0, year=0, id_school=0
        , school_dto=SchoolDto(), estado=0, nombre=''):
        self.Id = id
        self.Year = year
        self.IdSchool = id_school
        self.Estado = estado
        self.SchoolDto = school_dto
        self.Nombre = nombre

    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Year = json_data["Year"]
        self.IdSchool = json_data["IdSchool"]
        self.Estado = json_data["Estado"]