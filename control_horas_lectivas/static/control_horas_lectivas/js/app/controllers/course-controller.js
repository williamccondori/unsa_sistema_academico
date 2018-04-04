(function (module) {

    CourseController.$inject = ["$scope", "toastr", "CourseFactory"];

    function CourseController($scope, toastr, CourseFactory) {

        $scope.ListaCourse = [];

        $scope.ResetCourse = function () {
            $scope.Course = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetCourse();
            $scope.ObtenerCourse();
        };

        $scope.CrearCourse = function () {
            $scope.ResetCourse();
            $scope.Course.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-course');
        };

        $scope.ModificarCourse = function (modelo) {
            $scope.ResetCourse();
            $scope.Course = modelo;
            $scope.Course.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-course');
        };

        $scope.CancelarCourse = function () {
            Bootstrap.CerrarModal('#app-modal-course');
        };

        $scope.GuardarCourse = function () {
            CourseFactory.GuardarCourse($scope.Course).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerCourse();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-course');
        };

        $scope.EliminarCourse = function (modelo) {
            $scope.Course = modelo;
            CourseFactory.EliminarCourse($scope.Course).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerCourse();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerCourse = function () {
            CourseFactory.ObtenerCourse().then(function (response) {
                if (response.Estado)
                    $scope.ListaCourse = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

    }

    module.controller('CourseController', CourseController);

})(angular.module('app-unsa'));