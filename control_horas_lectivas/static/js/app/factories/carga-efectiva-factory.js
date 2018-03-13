(function (module) {
    CargaEfectivaFactory.$inject = [
        'BaseFactory'
    ];
    function CargaEfectivaFactory(BaseFactory) {
        var cargaEfectiva = [];
        cargaEfectiva.ObtenerCargaEfectiva = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/carga_efectiva');
        };
        return cargaEfectiva;
    }
    module.factory('CargaEfectivaFactory', CargaEfectivaFactory);
})(angular.module("app-unsa"));