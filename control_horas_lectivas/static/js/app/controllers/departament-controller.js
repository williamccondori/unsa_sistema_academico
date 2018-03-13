(function (module) {

    DepartamentController.$inject = ["$scope", "toastr", "DepartamentFactory"];

    function DepartamentController($scope, toastr, DepartamentFactory) {

        $scope.ListaDepartament = [];

        $scope.ResetDepartament = function () {
            $scope.Departament = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetDepartament();
            $scope.ObtenerDepartament();
        };

        $scope.CrearDepartament = function () {
            $scope.ResetDepartament();
            $scope.Departament.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-departament');
        };

        $scope.ModificarDepartament = function (modelo) {
            $scope.ResetDepartament();
            $scope.Departament = modelo;
            $scope.Departament.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-departament');
        };

        $scope.CancelarDepartament = function () {
            Bootstrap.CerrarModal('#app-modal-departament');
        };

        $scope.GuardarDepartament = function () {
            DepartamentFactory.GuardarDepartament($scope.Departament).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerDepartament();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-departament');
        };

        $scope.EliminarDepartament = function (modelo) {
            $scope.Departament = modelo;
            DepartamentFactory.EliminarDepartament($scope.Departament).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerDepartament();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerDepartament = function () {
            DepartamentFactory.ObtenerDepartament().then(function (response) {
                if (response.Estado)
                    $scope.ListaDepartament = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
    }

    module.controller('DepartamentController', DepartamentController);

})(angular.module('app-unsa'));