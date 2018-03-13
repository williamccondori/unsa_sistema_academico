from control_horas_lectivas.models import Course, Hour
from control_horas_lectivas.dtos.course_dto import CourseDto
from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.hour_dto import HourDto
from control_horas_lectivas.dtos.hour_type_dto import HourTypeDto
from control_horas_lectivas.dtos.teacher_dto import TeacherDto
import time

class CourseService(object):

    def get_by_study_plan(self, id_study_plan):
        
        courses = Course.objects.filter(study_plan_id=id_study_plan)

        time_s = time.time()

        courses_dto = list(map(lambda p: CourseDto(
            p.id,
            p.name,
            p.credit,
            p.study_plan_id,
            p.teacher_id,
            StudyPlanDto(),
            TeacherDto(
                p.teacher.id,
                p.teacher.name,
                p.teacher.address_name
            ),
            list(map(lambda d: HourDto(
                d.id,
                d.quantity,
                d.hour_type_id,
                HourTypeDto(
                    d.hour_type.id,
                    d.hour_type.name
                )
            ), p.hour_set.all()))
        ), courses))

        time_e = time.time()

        print('Se demoró'+ str(time_e - time_s))

        return courses_dto

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
