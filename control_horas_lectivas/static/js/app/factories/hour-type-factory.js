(function (module) {
    HourTypeFactory.$inject = [
        'BaseFactory'
    ];
    function HourTypeFactory(BaseFactory) {
        var hour_type = [];
        hour_type.ObtenerHourType = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/hour_type');
        };
        hour_type.GuardarHourType = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/hour_type', modelo);
        };
        hour_type.EliminarHourType = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/hour_type', modelo);
        };
        return hour_type;
    }
    module.factory('HourTypeFactory', HourTypeFactory);
})(angular.module("app-unsa"));