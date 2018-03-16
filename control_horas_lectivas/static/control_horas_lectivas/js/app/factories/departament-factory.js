(function (module) {
    DepartamentFactory.$inject = [
        'BaseFactory'
    ];
    function DepartamentFactory(BaseFactory) {
        var departament = [];
        departament.ObtenerDepartament = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/departament');
        };
        departament.GuardarDepartament = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/departament', modelo);
        };
        departament.EliminarDepartament = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/departament', modelo);
        };
        return departament;
    }
    module.factory('DepartamentFactory', DepartamentFactory);
})(angular.module("app-unsa"));