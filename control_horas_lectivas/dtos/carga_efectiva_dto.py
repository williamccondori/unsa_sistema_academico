from control_horas_lectivas.dtos.teacher_dto import TeacherDto

class CargaEfectivaDto(object):
    def __init__(self, teacher_dto=TeacherDto(), days_dto=[]):
        self.TeacherDto = teacher_dto
        self.DaysDto = days_dto
