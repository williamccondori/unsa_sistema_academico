(function (module) {
    HourFactory.$inject = [
        'BaseFactory'
    ];
    function HourFactory(BaseFactory) {
        var hour = [];
        hour.ObtenerHour = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/hour');
        };
        hour.GuardarHour = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/hour', modelo);
        };
        hour.EliminarHour = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/hour', modelo);
        };
        return hour;
    }
    module.factory('HourFactory', HourFactory);
})(angular.module("app-unsa"));