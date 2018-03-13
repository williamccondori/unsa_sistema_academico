
(function (module) {
    DayFactory.$inject = [
        'BaseFactory'
    ];
    function DayFactory(BaseFactory) {
        var day = [];
        day.ObtenerDay = function () {
            return BaseFactory.Obtener('/control_horas_lectivas/api/day');
        };
        day.GuardarDay = function (modelo) {
            return BaseFactory.Guardar('/control_horas_lectivas/api/day', modelo);
        };
        day.EliminarDay = function (modelo) {
            return BaseFactory.Eliminar('/control_horas_lectivas/api/day', modelo);
        };
        return day;
    }
    module.factory('DayFactory', DayFactory);
})(angular.module("app-unsa"));