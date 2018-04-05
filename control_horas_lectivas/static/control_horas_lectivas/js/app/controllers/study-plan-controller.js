(function (module) {

    StudyPlanController.$inject = [
        "$scope", 
        "toastr", 
        "StudyPlanFactory",
        "SchoolFactory"
    ];

    function StudyPlanController($scope, toastr, StudyPlanFactory, SchoolFactory) {

        $scope.ListaStudyPlan = [];
        $scope.ListaSchool = [];

        $scope.ResetStudyPlan = function () {
            $scope.StudyPlan = {
                Id: 0,
                Year: 0,
                CoursesDto: [],
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetStudyPlan();
            $scope.ObtenerStudyPlan();
            $scope.ObtenerSchool();
        };

        $scope.CrearStudyPlan = function () {
            $scope.ResetStudyPlan();
            $scope.StudyPlan.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-study-plan');
        };

        $scope.ModificarStudyPlan = function (modelo) {
            $scope.ResetStudyPlan();
            $scope.StudyPlan = modelo;
            $scope.StudyPlan.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-study-plan');
        };

        $scope.CancelarStudyPlan = function () {
            Bootstrap.CerrarModal('#app-modal-study-plan');
        };

        $scope.GuardarStudyPlan = function () {
            StudyPlanFactory.GuardarStudyPlan($scope.StudyPlan).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerStudyPlan();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-study-plan');
        };

        $scope.EliminarStudyPlan = function (modelo) {
            $scope.StudyPlan = modelo;
            StudyPlanFactory.EliminarStudyPlan($scope.StudyPlan).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerStudyPlan();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerStudyPlan = function () {
            StudyPlanFactory.ObtenerStudyPlan().then(function (response) {
                if (response.Estado)
                    $scope.ListaStudyPlan = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

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
    }

    module.controller('StudyPlanController', StudyPlanController);

})(angular.module('app-unsa'));