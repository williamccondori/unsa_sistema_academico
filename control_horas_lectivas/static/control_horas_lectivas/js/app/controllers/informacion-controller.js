(function (module) {

    InformacionController.$inject = ["$scope", "toastr", "InformacionFactory", "StudyPlanFactory"];

    function InformacionController($scope, toastr, InformacionFactory, StudyPlanFactory) {
        
        $scope.ListaPlanEstudio = []
        
        $scope.Iniciar = function () {
            $scope.ObtenerInformacion();
            $scope.ObtenerPlanEstudio();
        };

        $scope.ObtenerInformacionUsuario = function(){
            console.log('Obteniendo información del usuario')
        }

        $scope.ObtenerPlanEstudio = function(){
            StudyPlanFactory.ObtenerStudyPlan().then(function (response) {
                if (response.Estado)
                    $scope.ListaPlanEstudio = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerInformacion = function(){
            InformacionFactory.ObtenerInformacion().then(function (response) {
                if (response.Estado){
                    $scope.Informacion = response.Datos;
                    ruta_imagen = document.getElementById('app-usuario-imagen').attributes['src'].value;
                    ruta_imagen = ruta_imagen + $scope.Informacion.Imagen;
                    document.getElementById('app-usuario-imagen').attributes['src'].value = ruta_imagen;
                    document.getElementById('app-usuario-username').innerHTML = $scope.Informacion.Username.toUpperCase();
                }
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        }
    }

    module.controller('InformacionController', InformacionController);

})(angular.module('app-unsa'));