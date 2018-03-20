(function (module) {
    InformacionFactory.$inject = [
        'BaseFactory'
    ];
    function InformacionFactory(BaseFactory) {
        var Informacion = [];
        Informacion.ObtenerInformacion = function (modelo) {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/informacion', modelo);
        };
        Informacion.GuardarInformacion = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/informacion', modelo);
        };
        Informacion.EliminarInformacion = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/informacion', modelo);
        };
        return Informacion;
    }
    module.factory('InformacionFactory', InformacionFactory);
})(angular.module("app-unsa"));