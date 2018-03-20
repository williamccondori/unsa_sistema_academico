(function (module) {
    StudyPlanFactory.$inject = [
        'BaseFactory'
    ];
    function StudyPlanFactory(BaseFactory) {
        var studyPlan = [];
        studyPlan.ObtenerStudyPlan = function (modelo) {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/study_plan', modelo);
        };
        studyPlan.GuardarStudyPlan = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/study_plan', modelo);
        };
        studyPlan.EliminarStudyPlan = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/study_plan', modelo);
        };
        return studyPlan;
    }
    module.factory('StudyPlanFactory', StudyPlanFactory);
})(angular.module("app-unsa"));