(function (module) {

    SemesterController.$inject = ["$scope", "toastr", "SemesterTypeFactory"
    , "SemesterNumberFactory"];

    function SemesterController($scope, toastr, SemesterTypeFactory
    , SemesterNumberFactory) {


        $scope.Iniciar = function () {
            $scope.ResetSemesterNumber();
            $scope.ResetSemesterType();
            $scope.ObtenerSemesterNumber();
            $scope.ObtenerSemesterType();
        };

        $scope.ListaSemesterNumber = [];

        $scope.ResetSemesterNumber = function () {
            $scope.SemesterNumber = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.CrearSemesterNumber = function () {
            $scope.ResetSemesterNumber();
            $scope.SemesterNumber.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-semester-number');
        };

        $scope.ModificarSemesterNumber = function (modelo) {
            $scope.ResetSemesterNumber();
            $scope.SemesterNumber = modelo;
            $scope.SemesterNumber.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-semester-number');
        };

        $scope.CancelarSemesterNumber = function () {
            Bootstrap.CerrarModal('#app-modal-semester-number');
        };

        $scope.GuardarSemesterNumber = function () {
            SemesterNumberFactory.GuardarSemesterNumber($scope.SemesterNumber).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSemesterNumber();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-semester-number');
        };

        $scope.EliminarSemesterNumber = function (modelo) {
            $scope.SemesterNumber = modelo;
            SemesterNumberFactory.EliminarSemesterNumber($scope.SemesterNumber).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSemesterNumber();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerSemesterNumber = function () {
            SemesterNumberFactory.ObtenerSemesterNumber().then(function (response) {
                if (response.Estado)
                    $scope.ListaSemesterNumber = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ListaSemesterType = [];

        $scope.ResetSemesterType = function () {
            $scope.SemesterType = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.CrearSemesterType = function () {
            $scope.ResetSemesterType();
            $scope.SemesterType.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-semester-type');
        };

        $scope.ModificarSemesterType = function (modelo) {
            $scope.ResetSemesterType();
            $scope.SemesterType = modelo;
            $scope.SemesterType.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-semester-type');
        };

        $scope.CancelarSemesterType = function () {
            Bootstrap.CerrarModal('#app-modal-semester-type');
        };

        $scope.GuardarSemesterType = function () {
            SemesterTypeFactory.GuardarSemesterType($scope.SemesterType).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSemesterType();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-semester-type');
        };

        $scope.EliminarSemesterType = function (modelo) {
            $scope.SemesterType = modelo;
            SemesterTypeFactory.EliminarSemesterType($scope.SemesterType).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSemesterType();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerSemesterType = function () {
            SemesterTypeFactory.ObtenerSemesterType().then(function (response) {
                if (response.Estado)
                    $scope.ListaSemesterType = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
    }

    module.controller('SemesterController', SemesterController);

})(angular.module('app-unsa'));