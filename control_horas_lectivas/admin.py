from django.contrib import admin
from control_horas_lectivas.models import Departament
from control_horas_lectivas.models import Category
from control_horas_lectivas.models import Regime
from control_horas_lectivas.models import Teacher
from control_horas_lectivas.models import Course
from control_horas_lectivas.models import HourType
from control_horas_lectivas.models import Hour
from control_horas_lectivas.models import UserType
from control_horas_lectivas.models import UserSystem
from control_horas_lectivas.models import TeacherUser

admin.site.register(UserType)
admin.site.register(UserSystem)
admin.site.register(TeacherUser)