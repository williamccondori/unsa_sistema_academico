from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto


class CourseDto(object):
    def __init__(self, id=0, nombre='', credito=0, id_plan_estudio=0, plan_estudio_x=StudyPlanDto,
                 docentes=[]):
        self.Id = id
        self.Nombre = nombre
        self.Credito = credito
        self.IdPlanEstudio = id_plan_estudio
        self.PlanEstudioX = plan_estudio_x
        self.DocenteS = docentes

    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Nombre = json_data["Nombre"]
        self.Credito = json_data["Credito"]
        self.IdPlanEstudio = 0
        self.Estado = json_data["Estado"]

    def from_json_delete(self, json_data):
        self.Id = json_data["Id"]
