(function (module) {

    DayController.$inject = ["$scope", "toastr", "DayFactory"];

    function DayController($scope, toastr, DayFactory) {

        $scope.ListaDay = [];

        $scope.ResetDay = function () {
            $scope.Day = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetDay();
            $scope.ObtenerDay();
        };

        $scope.CrearDay = function () {
            $scope.ResetDay();
            $scope.Day.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-day');
        };

        $scope.ModificarDay = function (modelo) {
            $scope.ResetDay();
            $scope.Day = modelo;
            $scope.Day.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-day');
        };

        $scope.CancelarDay = function () {
            Bootstrap.CerrarModal('#app-modal-day');
        };

        $scope.GuardarDay = function () {
            DayFactory.GuardarDay($scope.Day).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerDay();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-day');
        };

        $scope.EliminarDay = function (modelo) {
            $scope.Day = modelo;
            DayFactory.EliminarDay($scope.Day).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerDay();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerDay = function () {
            DayFactory.ObtenerDay().then(function (response) {
                if (response.Estado)
                    $scope.ListaDay = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

    }

    module.controller('DayController', DayController);

})(angular.module('app-unsa'));