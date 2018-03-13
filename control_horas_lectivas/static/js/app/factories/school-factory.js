(function (module) {
    SchoolFactory.$inject = [
        'BaseFactory'
    ];
    function SchoolFactory(BaseFactory) {
        var school = [];
        school.ObtenerSchool = function () {
            return BaseFactory.Obtener('/control_horas_lectivas/api/school');
        };
        school.GuardarSchool = function (modelo) {
            return BaseFactory.Guardar('/control_horas_lectivas/api/school', modelo);
        };
        school.EliminarSchool = function (modelo) {
            return BaseFactory.Eliminar('/control_horas_lectivas/api/school', modelo);
        };
        return school;
    }
    module.factory('SchoolFactory', SchoolFactory);
})(angular.module("app-unsa"));