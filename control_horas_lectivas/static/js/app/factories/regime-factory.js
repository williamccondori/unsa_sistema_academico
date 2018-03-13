(function (module) {
    RegimeFactory.$inject = [
        'BaseFactory'
    ];
    function RegimeFactory(BaseFactory) {
        var regime = [];
        regime.ObtenerRegime = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/regime');
        };
        regime.GuardarRegime = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/regime', modelo);
        };
        regime.EliminarRegime = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/regime', modelo);
        };
        return regime;
    }
    module.factory('RegimeFactory', RegimeFactory);
})(angular.module("app-unsa"));