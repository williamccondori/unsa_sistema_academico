(function (module) {
    SemesterTypeFactory.$inject = [
        'BaseFactory'
    ];
    function SemesterTypeFactory(BaseFactory) {
        var semesterType = [];
        semesterType.ObtenerSemesterType = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/semester_type');
        };
        semesterType.GuardarSemesterType = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/semester_type', modelo);
        };
        semesterType.EliminarSemesterType = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/semester_type', modelo);
        };
        return semesterType;
    }
    module.factory('SemesterTypeFactory', SemesterTypeFactory);
})(angular.module("app-unsa"));