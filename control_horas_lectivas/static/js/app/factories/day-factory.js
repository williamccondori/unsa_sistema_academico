
(function (module) {
    DayFactory.$inject = [
        'BaseFactory'
    ];
    function DayFactory(BaseFactory) {
        var day = [];
        day.ObtenerDay = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/day');
        };
        day.GuardarDay = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/day', modelo);
        };
        day.EliminarDay = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/day', modelo);
        };
        return day;
    }
    module.factory('DayFactory', DayFactory);
})(angular.module("app-unsa"));