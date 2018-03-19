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
        self.Name = json_data["Name"]
        self.Credit = json_data["Credit"]
        self.IdStudyPlan = json_data["IdStudyPlan"]
        self.IdTeacher = json_data["IdTeacher"]
        self.Estado = json_data["Estado"]

        hours_dto = []
        for hour in json_data["HoursDto"]:
            hour_dto = HourDto()
            hour_dto.to_dto(
                hour["Id"],
                hour["Quantity"],
                hour["IdHourType"],
                hour["Estado"]
            )
            hours_dto.append(hour_dto)
        self.HoursDto = hours_dto

    def from_json_delete(self, json_data):
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.Credit = json_data["Credit"]
        self.IdStudyPlan = json_data["IdStudyPlan"]
        self.IdTeacher = json_data["IdTeacher"]
        self.Estado = json_data["Estado"]
