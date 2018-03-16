(function (module) {
    StudyPlanFactory.$inject = [
        'BaseFactory'
    ];
    function StudyPlanFactory(BaseFactory) {
        var StudyPlan = [];
        StudyPlan.ObtenerStudyPlan = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/study_plan');
        };
        StudyPlan.GuardarStudyPlan = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/study_plan', modelo);
        };
        StudyPlan.EliminarStudyPlan = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/study_plan', modelo);
        };
        return StudyPlan;
    }
    module.factory('StudyPlanFactory', StudyPlanFactory);
})(angular.module("app-unsa"));