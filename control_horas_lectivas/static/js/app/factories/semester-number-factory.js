(function (module) {
    SemesterNumberFactory.$inject = [
        'BaseFactory'
    ];
    function SemesterNumberFactory(BaseFactory) {
        var semesterNumber = [];
        semesterNumber.ObtenerSemesterNumber = function () {
            return BaseFactory.Obtener('/control_horas_lectivas/api/semester_number');
        };
        semesterNumber.GuardarSemesterNumber = function (modelo) {
            return BaseFactory.Guardar('/control_horas_lectivas/api/semester_number', modelo);
        };
        semesterNumber.EliminarSemesterNumber = function (modelo) {
            return BaseFactory.Eliminar('/control_horas_lectivas/api/semester_number', modelo);
        };
        return semesterNumber;
    }
    module.factory('SemesterNumberFactory', SemesterNumberFactory);
})(angular.module("app-unsa"));