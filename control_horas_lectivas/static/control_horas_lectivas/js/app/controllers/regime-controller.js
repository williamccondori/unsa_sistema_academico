(function (module) {

    RegimeController.$inject = ["$scope", "toastr", "RegimeFactory"];

    function RegimeController($scope, toastr, RegimeFactory) {

        $scope.ListaRegime = [];

        $scope.ResetRegime = function () {
            $scope.Regime = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetRegime();
            $scope.ObtenerRegime();
        };

        $scope.CrearRegime = function () {
            $scope.ResetRegime();
            $scope.Regime.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-regime');
        };

        $scope.ModificarRegime = function (modelo) {
            $scope.ResetRegime();
            $scope.Regime = modelo;
            $scope.Regime.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-regime');
        };

        $scope.CancelarRegime = function () {
            Bootstrap.CerrarModal('#app-modal-regime');
        };

        $scope.GuardarRegime = function () {
            RegimeFactory.GuardarRegime($scope.Regime).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerRegime();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-regime');
        };

        $scope.EliminarRegime = function (modelo) {
            $scope.Regime = modelo;
            RegimeFactory.EliminarRegime($scope.Regime).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerRegime();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerRegime = function () {
            RegimeFactory.ObtenerRegime().then(function (response) {
                if (response.Estado)
                    $scope.ListaRegime = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

    }

    module.controller('RegimeController', RegimeController);

})(angular.module('app-unsa'));