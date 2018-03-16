(function (module) {
    SchoolFactory.$inject = [
        'BaseFactory'
    ];
    function SchoolFactory(BaseFactory) {
        var school = [];
        school.ObtenerSchool = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/school');
        };
        school.GuardarSchool = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/school', modelo);
        };
        school.EliminarSchool = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/school', modelo);
        };
        return school;
    }
    module.factory('SchoolFactory', SchoolFactory);
})(angular.module("app-unsa"));