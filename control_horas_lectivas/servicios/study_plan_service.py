from control_horas_lectivas.models import StudyPlan, Departament, School
from control_horas_lectivas.dtos.study_plan_dto import StudyPlanDto
from control_horas_lectivas.dtos.school_dto import SchoolDto

class StudyPlanService(object):

    def obtener_x_departamento(self, id_departamento):
        plan_estudios_dto = []
        departamentos = Departament.objects.filter(id=id_departamento)
        for departamento in departamentos:
            for escuela in departamento.school_set.all():
                for plan_estudio in escuela.studyplan_set.all():
                    plan_estudios_dto.append(StudyPlanDto(
                        id=plan_estudio.id,
                        year=plan_estudio.year,
                        nombre=escuela.name + ' [' + str(plan_estudio.year) + ']',
                        school_dto=SchoolDto(
                            id=escuela.id,
                            name=escuela.name
                        )
                    ))
        return plan_estudios_dto

    def get(self):
        study_plans_dto = []
        study_plans = StudyPlan.objects.all()

        for study_plan in study_plans:
            study_plans_dto.append(StudyPlanDto(
                study_plan.id
                , study_plan.year
                , study_plan.school_id
                , SchoolDto(
                    study_plan.school.id
                    , study_plan.school.name
                )
            ))
        return study_plans_dto

    def save(self, study_plan_dto):
        if (study_plan_dto.Estado == 1):
            study_plan = StudyPlan(
                year=study_plan_dto.Year
                , school_id=study_plan_dto.IdSchool
            )
            study_plan.save()
        elif (study_plan_dto.Estado == 2):
            study_plan = StudyPlan.objects.filter(pk=study_plan_dto.Id)
            study_plan.update(
                year=study_plan_dto.Year
                , school_id=study_plan_dto.IdSchool
            )
        else:
            return

    def delete(self, study_plan_dto):
        study_plan = StudyPlan.objects.filter(pk=study_plan_dto.Id)
        study_plan.delete()
