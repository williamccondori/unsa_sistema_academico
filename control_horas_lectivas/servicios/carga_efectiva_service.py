from control_horas_lectivas.models import Teacher, Day, UserSystem, TeacherUser
from control_horas_lectivas.dtos.carga_efectiva_dto import CargaEfectivaDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
from control_horas_lectivas.dtos.departament_dto import DepartamentDto
from control_horas_lectivas.dtos.category_dto import CategoryDto
from control_horas_lectivas.dtos.regime_dto import RegimeDto
from control_horas_lectivas.dtos.course_dto import CourseDto
from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.school_dto import SchoolDto

class CargaEfectivaService(object):
    def get(self, username):
        carga_efectiva_dto = CargaEfectivaDto()
        usuario_sistema = UserSystem.objects.filter(username=username)
        usuario_sistema = usuario_sistema[0]
        teacher_user = TeacherUser.objects.filter(user_system_id=usuario_sistema.id)
        if len(teacher_user) is 0:
            return carga_efectiva_dto
        teacher_user = teacher_user[0]

        carga_efectiva_dto.TeacherDto = TeacherDto(
            id=teacher_user.teacher.id,
            name=teacher_user.teacher.name,
            address_name=teacher_user.teacher.address_name
        )

        return carga_efectiva_dto