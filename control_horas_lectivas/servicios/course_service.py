from control_horas_lectivas.models import Course, Hour
from control_horas_lectivas.dtos.course_dto import CourseDto
from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
import time

class CourseService(object):

    def obtener_x_plan_estudio(self, id_plan_estudio):
        cursos_dto = []
        cursos = Course.objects.filter(study_plan_id=id_plan_estudio)
        for curso in cursos:
            docentes_dto = []
            docentes_x_curso = curso.teacher_set.all()
            for docente in docentes_x_curso:
                docentes_dto.append(TeacherDto(
                    id=docente.id,
                    name=docente.name,
                    address_name=docente.address_name
                ))
            cursos_dto.append(CourseDto(
                id=curso.id,
                nombre=curso.name,
                credito=curso.credit,
                id_plan_estudio=curso.studt_plan_id,
                plan_estudio_x=StudyPlanDto(),
                docentes=docentes_dto
            ))
        return cursos_dto


    def get_by_study_plan(self, id_study_plan):
        return []

    def save(self, course_dto):
        if (course_dto.Estado == 1):
            course = Course(
                name=course_dto.Name
                , credit=course_dto.Credit
                , study_plan_id=course_dto.IdStudyPlan
                , teacher_id=course_dto.IdTeacher
            )
            course.save()

            course_id = Course.objects.latest('id')

            for hour_dto in course_dto.HoursDto:
                if (hour_dto.Estado == 1):
                    hour = Hour(
                        course_id=course_id.id,
                        hour_type_id=hour_dto.IdHourType, 
                        quantity=hour_dto.Quantity
                    )
                    hour.save()

        elif (course_dto.Estado == 2):
            course = Course.objects.filter(pk=course_dto.Id)
            course.update(
                name=course_dto.Name
                , credit=course_dto.Credit
                , study_plan_id=course_dto.IdStudyPlan
                , teacher_id=course_dto.IdTeacher
            )
        else:
            return

    def delete(self, course_dto):
        course = Course.objects.filter(pk=course_dto.Id)
        course.delete()
