(function (module) {

    SchoolController.$inject = [
        "$scope", 
        "toastr", 
        "SchoolFactory",
        "DepartamentFactory"
    ];

    function SchoolController($scope, toastr, SchoolFactory, DepartamentFactory) {

        $scope.ListaSchool = [];
        $scope.ListaDepartament = [];

        $scope.ResetSchool = function () {
            $scope.School = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetSchool();
            $scope.ObtenerSchool();
            $scope.ObtenerDepartament();
        };

        $scope.CrearSchool = function () {
            $scope.ResetSchool();
            $scope.School.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-school');
        };

        $scope.ModificarSchool = function (modelo) {
            $scope.ResetSchool();
            $scope.School = modelo;
            $scope.School.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-school');
        };

        $scope.CancelarSchool = function () {
            Bootstrap.CerrarModal('#app-modal-school');
        };

        $scope.GuardarSchool = function () {
            SchoolFactory.GuardarSchool($scope.School).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSchool();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-school');
        };

        $scope.EliminarSchool = function (modelo) {
            $scope.School = modelo;
            SchoolFactory.EliminarSchool($scope.School).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerSchool();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerSchool = function () {
            SchoolFactory.ObtenerSchool().then(function (response) {
                if (response.Estado)
                    $scope.ListaSchool = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

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

    module.controller('SchoolController', SchoolController);

})(angular.module('app-unsa'));