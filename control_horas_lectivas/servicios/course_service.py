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
            cursos_dto.append(CourseDto(
                id=curso.id,
                nombre=curso.name,
                credito=curso.credit,
                id_plan_estudio=curso.study_plan_id,
                plan_estudio_x=StudyPlanDto() ,
                docentes=[]
            ))
        return cursos_dto


    def get_by_study_plan(self, id_study_plan):
        return []

    def save(self, course_dto):
        if (course_dto.Estado == 1):
            print(course_dto.IdPlanEstudio)
            course = Course(
                name=course_dto.Nombre
                , credit=course_dto.Credito
                , study_plan_id=course_dto.IdPlanEstudio
            )
            course.save()

        elif (course_dto.Estado == 2):
            course = Course.objects.filter(pk=course_dto.Id)
            course.update(
                name=course_dto.Nombre
                , credit=course_dto.Credito
            )
        else:
            return

    def delete(self, course_dto):
        course = Course.objects.filter(pk=course_dto.Id)
        course.delete()
