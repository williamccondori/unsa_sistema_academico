(function (module) {

    HourTypeController.$inject = ["$scope", "toastr", "HourTypeFactory"];

    function HourTypeController($scope, toastr, HourTypeFactory) {

        $scope.ListaHourType = [];

        $scope.ResetHourType = function () {
            $scope.HourType = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetHourType();
            $scope.ObtenerHourType();
        };

        $scope.CrearHourType = function () {
            $scope.ResetHourType();
            $scope.HourType.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-hour-type');
        };

        $scope.ModificarHourType = function (modelo) {
            $scope.ResetHourType();
            $scope.HourType = modelo;
            $scope.HourType.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-hour-type');
        };

        $scope.CancelarHourType = function () {
            Bootstrap.CerrarModal('#app-modal-hour-type');
        };

        $scope.GuardarHourType = function () {
            HourTypeFactory.GuardarHourType($scope.HourType).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerHourType();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-hour-type');
        };

        $scope.EliminarHourType = function (modelo) {
            $scope.HourType = modelo;
            HourTypeFactory.EliminarHourType($scope.HourType).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerHourType();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerHourType = function () {
            HourTypeFactory.ObtenerHourType().then(function (response) {
                if (response.Estado)
                    $scope.ListaHourType = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

    }

    module.controller('HourTypeController', HourTypeController);

})(angular.module('app-unsa'));