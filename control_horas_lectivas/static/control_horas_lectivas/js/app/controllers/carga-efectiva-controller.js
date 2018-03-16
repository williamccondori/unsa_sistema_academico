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

        $scope.MostrarCourseActivity = function(){
            Bootstrap.AbrirModal('#app-modal-course-activity');
        };

        $scope.OcultarCourseActivity = function(){
            Bootstrap.CerrarModal('#app-modal-course-activity');
        };
    }

    module.controller('CargaEfectivaController', CargaEfectivaController);

})(angular.module('app-unsa'));




