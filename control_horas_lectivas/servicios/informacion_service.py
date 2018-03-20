from control_horas_lectivas.models import UserSystem, StudyPlan
from control_horas_lectivas.dtos.informacion_dto import InformacionDto

class InformacionService(object):
    def obtener(self, username, id_departamento, id_plan_estudio):
        usuario_sistema = UserSystem.objects.filter(username=username)
        usuario_sistema = usuario_sistema[0]
        informacion_dto = InformacionDto(
            id=usuario_sistema.id,
            nombre=usuario_sistema.user.first_name+' '+usuario_sistema.user.last_name,
            cargo=usuario_sistema.user_type.name,
            imagen=usuario_sistema.image,
            nombre_departamento=usuario_sistema.departament.name,
            nombre_plan_estudio='No seleccionado'
        )
        if id_plan_estudio is not False:
            plan_estudio = StudyPlan.objects.filter(id=id_plan_estudio)
            plan_estudio = plan_estudio[0]
            informacion_dto.NombrePlanEstudio = plan_estudio.year
        return informacion_dto