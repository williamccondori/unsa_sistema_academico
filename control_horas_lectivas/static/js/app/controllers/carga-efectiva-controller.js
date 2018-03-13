(function (module) {

    CargaEfectivaController.$inject = ["$scope", "toastr", "CargaEfectivaFactory"];

    function CargaEfectivaController($scope, toastr, CargaEfectivaFactory) {

        $scope.Teacher = {}

        $scope.Iniciar = function () {
            $scope.ObtenerCargaEfectiva();
        };

        $scope.ObtenerCargaEfectiva = function () {
            CargaEfectivaFactory.ObtenerCargaEfectiva().then(function (response) {
                if (response.Estado){
                    var cargaEfectiva = response.Datos;

                    $scope.Teacher = cargaEfectiva.TeacherDto;
                }
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

    }

    module.controller('CargaEfectivaController', CargaEfectivaController);

})(angular.module('app-unsa'));




