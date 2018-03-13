from django.urls import path
from control_horas_lectivas.api_controllers.departament_api_controller import DepartamentApiController
from control_horas_lectivas.api_controllers.category_api_controller import CategoryApiController
from control_horas_lectivas.api_controllers.regime_api_controller import RegimeApiController
from control_horas_lectivas.api_controllers.teacher_api_controller import TeacherApiController
from control_horas_lectivas.api_controllers.day_api_controller import DayApiController
from control_horas_lectivas.api_controllers.semester_type_api_controller import SemesterTypeApiController
from control_horas_lectivas.api_controllers.semester_number_api_controller import SemesterNumberApiController
from control_horas_lectivas.api_controllers.school_api_controller import SchoolApiController
from control_horas_lectivas.api_controllers.study_plan_api_controller import StudyPlanApiController
from control_horas_lectivas.api_controllers.course_api_controller import CourseApiController
from control_horas_lectivas.api_controllers.hour_api_controller import HourApiController
from control_horas_lectivas.api_controllers.hour_type_api_controller import HourTypeApiController
from control_horas_lectivas.api_controllers.hour_activity_api_controller import HourActivityApiController
from control_horas_lectivas.api_controllers.carga_efectiva_api_controller import CargaEfectivaApiController


API_NAME = 'api_'

urlpatterns = [
    path('departament', DepartamentApiController.as_view(), name=API_NAME+'departament'),
    path('category', CategoryApiController.as_view(), name=API_NAME+'category'),
    path('regime', RegimeApiController.as_view(), name=API_NAME+'regime'),
    path('teacher', TeacherApiController.as_view(), name=API_NAME+'teacher'),
    path('day', DayApiController.as_view(), name=API_NAME+'day'),
    path('semester_type', SemesterTypeApiController.as_view(), name=API_NAME+'semester_type'),
    path('semester_number', SemesterNumberApiController.as_view(), name=API_NAME+'semester_number'),
    path('school', SchoolApiController.as_view(), name=API_NAME+'school'),
    path('study_plan', StudyPlanApiController.as_view(), name=API_NAME+'study_plan'),
    path('course', CourseApiController.as_view(), name=API_NAME+'course'),
    path('hour', HourApiController.as_view(), name=API_NAME+'hour'),
    path('hour_type', HourTypeApiController.as_view(), name=API_NAME+'hour_type'),
    path('hour_activity', HourActivityApiController.as_view(), name=API_NAME+'hour_activity'),
    path('carga_efectiva', CargaEfectivaApiController.as_view(), name=API_NAME+'carga_efectiva'), 
]
