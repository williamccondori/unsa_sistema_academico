from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto

class CourseDto(object):

    def __init__(self, id=0, name="", credit=0, id_study_plan=0, id_teacher=0
        , study_plan_dto=StudyPlanDto(), teacher_dto=TeacherDto(), hours_dto=[], estado = 0):
        self.Id = id
        self.Name = name
        self.Credit = credit
        self.IdStudyPlan = id_study_plan
        self.IdTeacher = id_teacher
        self.Estado = estado
        self.StudyPlanDto = study_plan_dto
        self.TeacherDto = teacher_dto
        self.HoursDto = hours_dto

    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.Credit = json_data["Credit"]
        self.IdStudyPlan = json_data["IdStudyPlan"]
        self.IdTeacher = json_data["IdTeacher"]
        self.Estado = json_data["Estado"]