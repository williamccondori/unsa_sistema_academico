(function (module) {

    CategoryController.$inject = ["$scope", "toastr", "CategoryFactory"];

    function CategoryController($scope, toastr, CategoryFactory) {

        $scope.ListaCategory = [];

        $scope.ResetCategory = function () {
            $scope.Category = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetCategory();
            $scope.ObtenerCategory();
        };

        $scope.CrearCategory = function () {
            $scope.ResetCategory();
            $scope.Category.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-category');
        };

        $scope.ModificarCategory = function (modelo) {
            $scope.ResetCategory();
            $scope.Category = modelo;
            $scope.Category.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-category');
        };

        $scope.CancelarCategory = function () {
            Bootstrap.CerrarModal('#app-modal-category');
        };

        $scope.GuardarCategory = function () {
            CategoryFactory.GuardarCategory($scope.Category).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerCategory();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-category');
        };

        $scope.EliminarCategory = function (modelo) {
            $scope.Category = modelo;
            CategoryFactory.EliminarCategory($scope.Category).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerCategory();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerCategory = function () {
            CategoryFactory.ObtenerCategory().then(function (response) {
                if (response.Estado)
                    $scope.ListaCategory = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
    }

    module.controller('CategoryController', CategoryController);

})(angular.module('app-unsa'));